import pytest

from pages.courses.courses_list_page import CoursesListPage
from pages.courses.create_course_page import CreateCoursePage


@pytest.mark.regression
@pytest.mark.courses
class TestCourses:
    def test_edit_course(self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
        create_course_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create')
        create_course_page.create_course_form.fill(
            title='Test Course',
            estimated_time='100',
            description='Test description',
            max_score='100',
            min_score='11'
        )
        create_course_page.image_upload_widget.upload_preview_image('./testdata/files/test_image.jpg')
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course_toolbar_view.click_create_course_button()
        courses_list_page.course_view.check_visible(
            index=0,
            title='Test Course',
            estimated_time='100',
            max_score='100',
            min_score='11'
        )
        courses_list_page.course_view.menu.click_edit(index=0)
        create_course_page.create_course_form.fill(
            title='Edited Test Course',
            estimated_time='123',
            description='Edited Test description',
            max_score='54321',
            min_score='12345'
        )
        create_course_page.create_course_toolbar_view.click_create_course_button()
        courses_list_page.course_view.check_visible(
            index=0,
            title='Edited Test Course',
            estimated_time='123',
            max_score='54321',
            min_score='12345'
        )

    def test_empty_courses_list(self, courses_list_page: CoursesListPage):
        courses_list_page.visit('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses')

        courses_list_page.navbar.check_visible('Andrey')
        courses_list_page.sidebar.check_visible()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.check_visible_empty_view()

    def test_create_course(self, create_course_page: CreateCoursePage, courses_list_page: CoursesListPage):
        create_course_page.visit("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses/create")

        create_course_page.create_course_toolbar_view.check_visible()
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=False)
        create_course_page.create_course_form.check_visible(
            title='',
            max_score='0',
            min_score='0',
            description='',
            estimated_time=''
        )

        create_course_page.create_course_exercises_toolbar_view.check_visible()
        create_course_page.check_visible_exercise_empty_view()
        create_course_page.image_upload_widget.upload_preview_image('./testdata/files/test_image.jpg')
        create_course_page.image_upload_widget.check_visible(is_image_uploaded=True)
        create_course_page.create_course_form.fill(
            title='Playwright',
            max_score='100',
            min_score='10',
            description='Playwright',
            estimated_time='2 weeks'
        )
        create_course_page.create_course_toolbar_view.click_create_course_button()

        courses_list_page.toolbar_view.check_visible()
        courses_list_page.course_view.check_visible(
            index=0,
            title='Playwright',
            max_score='100',
            min_score='10',
            estimated_time='2 weeks'
        )