__author__ = 'fhca'


# suma = 0
#
# for x in range(1, 101):
#     suma = suma + x
#
# print("La suma es:", suma)


def sumatoria(a, b):
    suma = 0
    for x in range(a, b + 1):
        suma = suma + x
    print("La suma es:", suma)


# 20->30,  70->90,  110->300,  425->440, 12->900

sumatoria(20, 30)
sumatoria(70, 90)
sumatoria(110, 300)
sumatoria(425, 440)
sumatoria(12, 900)
