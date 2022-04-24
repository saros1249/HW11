# Утилиты для проекта Домашняя работа - 11 урока.
import json


def load_candidates_from_json():
    '''
    Из файла json возвращает список словарей.
    '''

    with open('candidates.json', 'r', encoding='utf8') as file:
        return json.load(file)


def get_candidate(candidate_id):
    '''
    Возвращает одного кандидата по id
    :param candidate_id:
    :return: словарь
    '''
    candidate_list = load_candidates_from_json()
    for i in range(len(candidate_list)):
        if candidate_id == candidate_list[i]['id']:
            return {'name': candidate_list[i]['name'], 'position': candidate_list[i]['position'],
                    'picture': candidate_list[i]['picture'], 'skills': candidate_list[i]['skills']}


def get_candidates_by_name(candidate_name):
    '''
    Возвращает кандидиатов по имени и подсчитывает количество кандидатов с одним именем
    :param candidate_name:
    :return: list
    '''
    candidate_list = load_candidates_from_json()
    name_candidate = []
    for i in range(len(candidate_list)):
        if candidate_name in candidate_list[i]['name']:
            name_candidate.append(candidate_list[i]['name'])
    return name_candidate


def get_candidates_by_skill(skill_name):
    '''
    Возвращает кандидиатов по skill
    :param skill_name:
    :return: list
    '''
    candidate_list = load_candidates_from_json()
    skill_candidate_name = []
    for i in range(len(candidate_list)):
        if skill_name in candidate_list[i]['skills'].lower().split(', '):
            skill_candidate_name.append(candidate_list[i]['name'])
    return skill_candidate_name
