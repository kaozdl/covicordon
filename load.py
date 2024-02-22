import csv

from members.models import Member

socios = csv.DictReader(open('socios.csv'))
socios_list = []

for row in socios:
    socios_list.append(row)

for s in socios_list:
    if s["Activo"] == "Si":
        socio = Member(
            first_name=s["Nombre"],
            last_name=s["Apellido"],
            member_number=s["Nro de Socio"],
            apartment_number=s["Apto"],
            bedrooms=s["Dorm."],
        )
        socio.save()
