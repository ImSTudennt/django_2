from rest_framework.test import APIClient
import pytest
from model_bakery import baker
from students.models import Student, Course
from pprint import pprint


@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def student_factory():
    def factory(*args,**kwargs):
        return baker.prepare(Student, *args, **kwargs)
    
    return factory

@pytest.fixture
def course_factory(student_factory):
    def factory(*args,**kwargs):
        student_set = student_factory(_quantity=5)
        return baker.make(Course, students=student_set, *args, **kwargs, make_m2m=True)
    
    return factory


@pytest.mark.django_db
def test_get_course(client, course_factory):

    course = course_factory(_quantity=1)

    response = client.get('/api/v1/courses/')
    
    assert response.status_code == 200
    assert len(course) == len(response.json())
    assert response.json()[0]['name'] == course[0].name

@pytest.mark.django_db
def test_list_courses(client, course_factory):

    courses = course_factory(_quantity=5)

    response = client.get('/api/v1/courses/').json()

    assert len(courses) == len(response)
    assert type(courses) == list


@pytest.mark.django_db
def test_filterid(client, course_factory):

    courses = course_factory(_quantity=5)
    find_id = 9

    response = client.get(f'/api/v1/courses/?id={find_id}')
    assert response.status_code == 200
    assert response.json()[0]['id'] == 9 

@pytest.mark.django_db
def test_filter_name(client, course_factory):

    courses = course_factory(_quantity=5)

    for el in courses:
        name = el.name
        response = client.get(f'/api/v1/courses/?name={name}')
        assert el.id == response.json()[0]['id']


@pytest.mark.django_db
def test_post(client):
    
    student = Student.objects.create(name='Valya')
    count = Course.objects.count()
    response = client.post('/api/v1/courses/', {'name': 'Python', 'students': [student.id]})
    assert response.status_code == 201
    assert  Course.objects.count() == count + 1


@pytest.mark.django_db
def test_patch(client):
    
    client.post('/api/v1/courses/', {'name': 'Pythod'})
    assert Course.objects.filter(id=18)[0].name == 'Pythod'
    response = client.patch('/api/v1/courses/18/', {'name': 'Java'})
    
    assert response.status_code == 200
    assert Course.objects.filter(id=18)[0].name == 'Java' 


@pytest.mark.django_db
def test_delete(client):
    
    client.post('/api/v1/courses/', {'name': 'Uni'})
    count = Course.objects.count()
    response = client.delete('/api/v1/courses/19/')
    
    assert response.status_code == 204
    assert Course.objects.count() == count - 1








