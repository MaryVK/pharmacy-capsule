from dataclasses import dataclass

@dataclass
class Capsule:
   active_ingredient: str
   __dosage_mg: float
   is_dissolved: bool
   is_expired: bool

   def __post_init__(self):
       self.dosage_mg = self.__dosage_mg

   @property
   def dosage_mg(self) -> float:
       return self.__dosage_mg

   @dosage_mg.setter
   def dosage_mg(self, value: float):
       if value <= 0:
           raise ValueError("Дозировка лекарства не может быть нулевой или отрицательной!")
       self.__dosage_mg = float(value)


   # метод с валидацией
   def dissolve(self) -> None:
       if self.is_expired:
           raise ValueError("Невозможно разбавить: Ваше лекарство просрочилось!")
       else:
           self.is_dissolved = True
           print(f"Капсула {self.active_ingredient} успешно растворилась в Вашем желудке!")

   # обычный метод
   def check_safety(self) -> bool:
       if self.is_expired:
           print("Капсула просрочена и Вы можете умереть!")
           return False
       else:
           print("Капсула безопасна, можно глотать")
           return True

   # обычный метод
   def calculate_intake(self, patient_weight_kg: float) -> int:
       if patient_weight_kg <= 0:
           raise ValueError("У пациента должен быть какой-то вес!")

       # 10 мг на 1 кг веса чел-ка
       required_mg = patient_weight_kg * 10
       capsules_needed = max(1, round(required_mg / self.dosage_mg))
       print(f"Для веса {patient_weight_kg} кг рекомендуется принять {capsules_needed} капсул")
       return capsules_needed

   # обычный метод
   # если чел. выпил алкогольн.напиток, то есть препараты, кот. категорически запрещено принимать
   def ckeck_alcohol_compatibility(self) -> bool:
       dangerous_drugs = ["Antibiotic", "Paracetamol", "Analgin", "Ibuprofen"]

       if self.active_ingredient in dangerous_drugs:
           print(f"КРИТИЧЕСКИ ОПАСНО: {self.active_ingredient} несовместим с алкоголем!")
           return False

   # обычный метод
   def print_status(self) -> None:
       print(f"Препарат: {self.active_ingredient}")
       print(f"Дозировка: {self.dosage_mg}")
       print(f"Растворимость: {self.is_dissolved}")
       print(f"Срок годности: {self.is_expired}")
