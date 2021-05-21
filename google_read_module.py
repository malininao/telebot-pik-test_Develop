from pprint import pprint
import httplib2
import googleapiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
from collections import defaultdict
import os


def create_keyfile_dict():
    variables_keys = {
        "type": os.environ.get("SHEET_TYPE"),
        "project_id": os.environ.get("SHEET_PROJECT_ID"),
        "private_key_id": os.environ.get("SHEET_PRIVATE_KEY_ID"),
        "private_key": os.environ.get("SHEET_PRIVATE_KEY"),
        "client_email": os.environ.get("SHEET_CLIENT_EMAIL"),
        "client_id": os.environ.get("SHEET_CLIENT_ID"),
        "auth_uri": os.environ.get("SHEET_AUTH_URI"),
        "token_uri": os.environ.get("SHEET_TOKEN_URI"),
        "auth_provider_x509_cert_url": os.environ.get("SHEET_AUTH_PROVIDER_X509_CERT_URL"),
        "client_x509_cert_url": os.environ.get("SHEET_CLIENT_X509_CERT_URL")
    }
    return variables_keys


HEROKU = os.environ.get('HEROKU')
if HEROKU == "True":
    CREDENTIALS_FILE = create_keyfile_dict()
else:
    CREDENTIALS_FILE = 'osipia-eac8c331dd32.json'

scope = ['https://www.googleapis.com/auth/drive',
         'https://www.googleapis.com/auth/documents.readonly']
credentional = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    scope
)
httpAuth = credentional.authorize(httplib2.Http())
services = googleapiclient.discovery.build('docs', 'v1', http=httpAuth)


class GoogleDocs:

    # Класс который получает необходимые блоки гугл документа для дальнейшей работы в другом классе
    def __init__(self, link_url):
        self.lnk = link_url

    def get_document_from_url(self):
        docs_id = self.lnk.split('/')[5]
        document = services.documents().get(documentId=docs_id).execute()
        return document

    def get_document_body(self):
        doc_body = self.get_document_from_url().get('body')
        return doc_body

    def get_inline_object(self):
        inline_object = self.get_document_from_url().get('inlineObjects')
        return inline_object


class GoogleDocsRead:

    def __init__(self, doc_body=None, inline_objects=None, document_style=None, named_styles=None,
                 revision_id=None, suggestions_view_mode=None, document_id=None):

        self.doc_body = doc_body
        self.document_style = document_style
        self.inline_objects = inline_objects
        self.named_styles = named_styles
        self.revision_id = revision_id
        self.suggestions_view_mode = suggestions_view_mode
        self.document_id = document_id

    @staticmethod
    def build_in_html(text, styles):
        #print(styles)
        if 'italic' in styles:
            text = f'<i>{text}</i>'
        if 'bold' in styles:
            text = f'<b>{text}</b>'
        if 'underline' in styles:
            text = f'<u>{text}</u>'
        return text

    def read_text(self):
        # print(str(docBody['content'][2]['paragraph']['elements'][1]))

        paragraph_count = int(str(self.doc_body).count('paragraph') / 2)
        total_text_list = []

        for i in range(1, paragraph_count + 1, 1):
            string = ''
            elements_count = len(list(self.doc_body['content'][i]['paragraph']['elements']))

            for j in range(0, elements_count, 1):
                if str(self.doc_body['content'][i]['paragraph']['elements'][j]).count("inlineObjectElement") == 0:
                    text = self.doc_body['content'][i]['paragraph']['elements'][j]['textRun']['content']
                    styles = self.doc_body['content'][i]['paragraph']['elements'][j]['textRun']['textStyle']
                    string = string + self.build_in_html(text=text, styles=styles)
            total_text_list.append(string.replace('\n', ''))

            # if '' in total_text_list:
            # total_text_list.remove('')

        # print(total_text_list)

        return total_text_list

    def get_img(self):

        paragraph_count = int(str(self.doc_body).count('paragraph') / 2)
        total_img_list = []

        for i in range(1, paragraph_count + 1, 1):
            img_url = ''
            elements_count = len(list(self.doc_body['content'][i]['paragraph']['elements']))

            for j in range(0, elements_count, 1):
                if str(self.doc_body['content'][i]['paragraph']['elements'][j]).count("inlineObjectElement") != 0:
                    img_id = self.doc_body['content'][i]['paragraph']['elements'][j]['inlineObjectElement'] \
                        ['inlineObjectId']
                    img_url = (self.inline_objects[f'{img_id}']['inlineObjectProperties']['embeddedObject']
                    ['imageProperties']['contentUri'])

            total_img_list.append(img_url.replace('\n', ''))

            # if '' in total_img_list:
            # total_img_list.remove('')

        # print(total_img_list)

        return total_img_list

    def join_total_list(self):
        text_list = self.read_text()
        img_list = self.get_img()

        index_empty_text = defaultdict(list)
        index_empty_url = defaultdict(list)

        for index, e in enumerate(text_list):
            index_empty_text[e].append(index)

        for index, e in enumerate(img_list):
            index_empty_url[e].append(index)

        total_list = []
        for i in range(len(text_list)):
            total_list.append(text_list[i])
            total_list.append(img_list[i])
            if '' in total_list:
                total_list.remove('')
        if '' in total_list:
            total_list.remove('')

        for i in range(len(total_list)):
            if '' in total_list:
                total_list.remove('')

        '''
        print(index_empty_text)
        print(index_empty_url)
    
        print(index_empty_text[''])
        print(index_empty_url[''])
        '''
        #print(total_list)

        return total_list


if __name__ == "__main__":
    linkURL = 'https://docs.google.com/document/d/1yb7TAgQQqjhBWoiCEmlRx0iZWbOp7BmHVxbRA_Ubl_k/edit'
    doc = GoogleDocs(linkURL)
    instruction = GoogleDocsRead(doc_body=doc.get_document_body(),
                                 inline_objects=doc.get_inline_object()).join_total_list()
