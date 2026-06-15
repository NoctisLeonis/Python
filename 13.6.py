cars = {
    "Лада Веста": 175,
    "Toyota Camry": 210,
    "Hyundai Solaris": 185,
    "Kia Rio": 178,
    "Volkswagen Polo": 182,
    "BMW M5": 250,
    "Audi A6": 240,
    "Mercedes E-Class": 250,
    "Renault Logan": 170,
    "Skoda Octavia": 195,
    "Mazda 6": 205,
    "Ford Focus": 180,
    "Honda Civic": 200,
    "Nissan Almera": 168,
    "Chevrolet Cruze": 183,
    "Mitsubishi Lancer": 177,
    "Subaru Impreza": 190,
    "Opel Astra": 182,
    "Peugeot 308": 181,
    "Suzuki Vitara": 173,
}
print("Модели со скоростью выше 180 км/ч:")
for model, speed in cars.items():
    if speed > 180:
        print(f"- {model} ({speed} км/ч)")