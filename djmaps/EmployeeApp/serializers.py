#Converts the complex model instances into native python datatypes, that can then be easily
#that can then be rendered into json or xmls or others. Also help with serialization (past data into complex types)
from rest_framework import serializers

from EmployeeApp.models import Departments, Employees

class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departments
        fields=("DepartmentId", "DepartmentName")
class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees
        fields = ('EmployeeId', 'EmployeeName', 'DateOfJoining', 'PhotoFileName')