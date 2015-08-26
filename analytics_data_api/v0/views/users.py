"""
API methods for user data.
"""
from rest_framework import generics

from analytics_data_api.v0.models import StudentGrade, UserProfile
from analytics_data_api.v0.serializers import StudentGradeSerializer


class UserGradesView(generics.ListAPIView):
    """
    Get this user's grades in all courses where grade information is available.

    **Example Request**

        GET /api/v0/users/{username}/grades/

    **Response Values**

        Returns a list of StudentGrade objects wich have these properties:

            * course_id: The course in which this grade has been earned (string)
            * user_id: The user's ID (integer)
            * letter_grade: The user's letter grade or null if the user is not passing (string)
            * percent_grade: The user's grade as a percentage (0-100, float)
            * is_passing: Whether or not the user is passing this course (boolean)
            * created: When this grade was last updated in the analytics database (datetime)
        """

    serializer_class = StudentGradeSerializer

    def get_queryset(self):
        """Select the view count for a specific module"""
        username = self.kwargs.get('username')
        user = UserProfile.objects.get(username=username)
        return StudentGrade.objects.filter(user_id=user.pk)
