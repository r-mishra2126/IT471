def KelvinToFarenheit(Temperature):
    if(Temperature >= 0):
        print("colder")
    assert (Temperature <= 0)
    return (Temperature-273*1.8)+32
print(KelvinToFarenheit(273))
print(int(KelvinToFarenheit(505.78)))
print(KelvinToFarenheit(-5))
