import requests

base_url = "https://yougile.com/api-v2/"

#посмотреть список всех проектов
def get_projekt_list():     
    my_headers={}
    my_headers['Authorization'] = "Bearer Dkcq15X6WrjfHw200u4VpZ2C8fSJFHnNlSvzyVBlVnVVVrjUp3cchLXuSFmxeU1w"
    resp = requests.get(base_url+'projects', headers=my_headers)
    return resp.json()

#добавить новый проект
users={'dcf300fb-9f9c-422d-bd90-5c094c45ca09': 'admin'}
name='Старое название проекта'
def add_new_proect(name, users): 
    newproject={
        'title' : name,
        'users' : users
    }

    my_headers={}
    my_headers['Authorization'] = "Bearer Dkcq15X6WrjfHw200u4VpZ2C8fSJFHnNlSvzyVBlVnVVVrjUp3cchLXuSFmxeU1w"

    new_project=requests.post(base_url+'projects', json=newproject, headers=my_headers)
    proect_id=new_project.json() 
    return proect_id  

#посмотреть проект по id
def get_projekt_id():     
    body=get_projekt_list()
    my_headers={}
    my_headers['Authorization'] = "Bearer Dkcq15X6WrjfHw200u4VpZ2C8fSJFHnNlSvzyVBlVnVVVrjUp3cchLXuSFmxeU1w"
    my_proect_id = body['content'][-1]['id']
    resp_body = requests.get(base_url+'projects/'+str(my_proect_id), headers=my_headers)
    return resp_body.json()

#изменить проект
def change_proects(new_name, users):
    my_headers={}
    my_headers['Authorization'] = "Bearer Dkcq15X6WrjfHw200u4VpZ2C8fSJFHnNlSvzyVBlVnVVVrjUp3cchLXuSFmxeU1w"
    project = {
        'deleted': False,
        'title': new_name,
        'users': users
    }
    proect_id = get_projekt_list()['content'][-1]['id']
    change_project=requests.put(base_url+'projects/'+str(proect_id), json=project, headers=my_headers)
    return change_project.json() 
        

def test_add_new_proekt():
    body = get_projekt_list()
    len_before = body["paging"]["count"]
    name='новье'
    add_new_proect(name, users)
    body = get_projekt_list()
    len_after = body["paging"]["count"]
    assert len_after - len_before == 1
    assert body["content"][-1]["title"] == name

def test_add_new_proekt_negativ():
    body = get_projekt_list()
    len_before = body["paging"]["count"]
    name=''
    add_new_proect(name, users)
    body = get_projekt_list()
    len_after = body["paging"]["count"]
    assert len_after == len_before
   
def test_change_proekt():
    add_new_proect(name,users)
    body = get_projekt_list()
    len_before = len(body["content"]) 
    new_name='Поменяли название проекта'
    change_proects(new_name, users)
    body = get_projekt_list()
    len_after = len(body["content"])  
    assert len_after == len_before
    assert body["content"][-1]["title"] == new_name   

def test_change_proekt_negative():
    add_new_proect(name,users)
    body = get_projekt_list()
    len_before = len(body["content"]) 
    new_name=''
    change_proects(new_name, users)
    body = get_projekt_list()
    len_after = len(body["content"])  
    assert len_after == len_before
    assert body["content"][-1]["title"] == name

#посмотреть проект по id
def test_get_proect_id ():
    add_new_proect(name, users)
    body=get_projekt_list()
    my_headers={}
    my_headers['Authorization'] = "Bearer Dkcq15X6WrjfHw200u4VpZ2C8fSJFHnNlSvzyVBlVnVVVrjUp3cchLXuSFmxeU1w"
    my_proect_id = body['content'][-1]['id']
    resp_body = requests.get(base_url+'projects/'+str(my_proect_id), headers=my_headers)
    assert resp_body.status_code == 200

def test_get_proect_id_negative ():
    add_new_proect(name, users)
    body=get_projekt_list()
    my_proect_id = body['content'][-1]['id']
    resp_body = requests.get(base_url+'projects/'+str(my_proect_id))
    assert resp_body.status_code == 401

    



   