from pprint import pprint
import httplib2
import googleapiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials
from collections import defaultdict

CREDENTIALS_FILE = 'osipia-eac8c331dd32.json'
credentional = ServiceAccountCredentials.from_json_keyfile_name(
        CREDENTIALS_FILE,
        ['https://www.googleapis.com/auth/drive',
         'https://www.googleapis.com/auth/documents.readonly']
    )
httpAuth = credentional.authorize(httplib2.Http())
services = googleapiclient.discovery.build('docs', 'v1', http=httpAuth)


class GoogleDocs:

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

    def __init__(self, link_url):
        self.lnk = link_url


def read_text(doc_body):
    #print(str(docBody['content'][2]['paragraph']['elements'][1]))

    paragraph_count = int(str(doc_body).count('paragraph')/2)
    total_text_list = []

    for i in range(1, paragraph_count+1, 1):
        string = ''
        elements_count = len(list(doc_body['content'][i]['paragraph']['elements']))

        for j in range(0, elements_count, 1):
            if str(doc_body['content'][i]['paragraph']['elements'][j]).count("inlineObjectElement") == 0:
                text = doc_body['content'][i]['paragraph']['elements'][j]['textRun']['content']
                string = string + text
        total_text_list.append(string.replace('\n', ''))

        #if '' in total_text_list:
            #total_text_list.remove('')

    #print(total_text_list)

    return total_text_list


def get_img(doc_body, inline_object):

    paragraph_count = int(str(doc_body).count('paragraph') / 2)
    total_img_list = []

    for i in range(1, paragraph_count + 1, 1):
        img_url = ''
        elements_count = len(list(doc_body['content'][i]['paragraph']['elements']))

        for j in range(0, elements_count, 1):
            if str(doc_body['content'][i]['paragraph']['elements'][j]).count("inlineObjectElement") != 0:
                img_id = doc_body['content'][i]['paragraph']['elements'][j]['inlineObjectElement']['inlineObjectId']
                img_url = (inline_object[f'{img_id}']['inlineObjectProperties']['embeddedObject']
                    ['imageProperties']['contentUri'])

        total_img_list.append(img_url.replace('\n', ''))

        #if '' in total_img_list:
            #total_img_list.remove('')

    #print(total_img_list)

    return total_img_list


def join_total_list(tetx_list, img_list):
    text_list = tetx_list
    img_list = img_list

    index_empty_text = defaultdict(list)
    index_empty_url = defaultdict(list)

    for index, e in enumerate(tetx_list):
        index_empty_text[e].append(index)

    for index, e in enumerate(img_list):
        index_empty_url[e].append(index)

    total_list = []
    for i in range(len(text_list)):
        total_list.append(text_list[i])
        total_list.append(img_list[i])
        if '' in total_list:
            total_list.remove('')
    total_list.remove('')

    for i in range(len(total_list)):
        if '' in total_list:
            total_list.remove('')

    '''
    print(index_empty_text)
    print(index_empty_url)

    print(index_empty_text[''])
    print(index_empty_url[''])

    print(total_list)
    '''
    return total_list


if __name__ == "__main__":
    linkURL = 'https://docs.google.com/document/d/1EJinayuOfj1-ZPJUdEXNh7-Ny0LJrCnz0H5E-W3poM8/edit'
    doc = GoogleDocs(linkURL)
    read_text(doc.get_document_body())
    get_img(doc.get_document_body(), doc.get_inline_object())
    join_total_list(read_text(doc.get_document_body()),
                    get_img(doc.get_document_body(), doc.get_inline_object()))


