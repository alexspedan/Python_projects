test_str = 'Посмотрите на сценарий ниже и ответьте на вопрос: "Подходит ли в этом сценарии использование докера? Или лучше подойдет виртуальная машина, физическая машина? Или возможны разные варианты?'
print(test_str.split('?'))

raw_input = 'Tenet'
clear_input = raw_input.lower()
reflected_input = clear_input[::-1]
print(clear_input)
print(reflected_input)
if clear_input == reflected_input:
  print(raw_input + ' is polyndrome')
else:
  print(raw_input + ' is not polyndrome')
