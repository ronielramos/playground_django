import datetime
from typing import NewType, Optional

QuestionsForAuto = NewType('QuestionsForAuto', {
    'vehicle': { 
      'year': int
    },
    'income': int
})

class AutoInsurance:
  def __init__(self, questions: QuestionsForAuto):
    self.__income_count = self.__has_income(questions['income'])
    self.__produced_count = False if ('vehicle' not in questions) else self.__produced_more_than_five_years(
        questions['vehicle']['year'])


  def __has_income(self, income: int) -> bool: return income > 0
  

  def __has_vehicle(self, vehicle: { 'year': int }) -> bool: return vehicle is None


  def __produced_more_than_five_years(self, produced_year: int) -> bool:
    return False if produced_year == None else 5 >= (datetime.date.today().year - produced_year)


  def get_score(self) -> Optional[int]:
    if (self.__income_count == False): return None 
    if (self.__produced_count == False): return 0
    return 1


auto_insurance = AutoInsurance({
    'income': 400
  })

print(auto_insurance.get_score())


