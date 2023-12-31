import numpy as np


# Вхідні дані (вхідні дані для кожної букви)
X = np.array([[0, 0, 1, 1, 1, 1, 0, 0,  # 'А'
               0, 1, 0, 0, 0, 0, 1, 0,
               0, 1, 0, 0, 0, 0, 1, 0,
               0, 1, 1, 1, 1, 1, 1, 0,
               0, 1, 0, 0, 0, 0, 1, 0,
               0, 1, 0, 0, 0, 0, 1, 0,
               0, 1, 0, 0, 0, 0, 1, 0],

              [0, 1, 1, 1, 1, 1, 1, 0,  # 'Б'
               0, 1, 0, 0, 0, 0, 0, 0,
               0, 1, 0, 0, 0, 0, 0, 0,
               0, 1, 1, 1, 1, 1, 0, 0,
               0, 1, 0, 0, 0, 0, 1, 0,
               0, 1, 0, 0, 0, 0, 1, 0,
               0, 1, 1, 1, 1, 1, 0, 0],
              
              [0, 1, 1, 1, 1, 1, 0, 0,  # 'В'
               0, 1, 0, 0, 0, 0, 1, 0,
               0, 1, 0, 0, 0, 0, 1, 0,
               0, 1, 1, 1, 1, 1, 0, 0,
               0, 1, 0, 0, 0, 0, 1, 0,
               0, 1, 0, 0, 0, 0, 1, 0,
               0, 1, 1, 1, 1, 1, 0, 0],
              
              [0, 1, 1, 1, 1, 1, 1, 0,  # 'Г'
               0, 1, 0, 0, 0, 0, 0, 0,
               0, 1, 0, 0, 0, 0, 0, 0,
               0, 1, 0, 0, 0, 0, 0, 0,
               0, 1, 0, 0, 0, 0, 0, 0,
               0, 1, 0, 0, 0, 0, 0, 0,
               0, 1, 0, 0, 0, 0, 0, 0],
               
              [0, 0, 0, 0, 0, 0, 1, 0,  # 'Ґ'
               0, 1, 1, 1, 1, 1, 1, 0,
               0, 1, 0, 0, 0, 0, 0, 0,
               0, 1, 0, 0, 0, 0, 0, 0,
               0, 1, 0, 0, 0, 0, 0, 0,
               0, 1, 0, 0, 0, 0, 0, 0,
               0, 1, 0, 0, 0, 0, 0, 0],
              
              [0, 1, 1, 1, 1, 1, 1, 0,  # 'Д'
               0, 1, 0, 0, 0, 0, 1, 0,
               0, 1, 0, 0, 0, 0, 1, 0,
               0, 1, 0, 0, 0, 0, 1, 0,
               0, 1, 1, 1, 1, 1, 1, 0,
               1, 0, 0, 0, 0, 0, 0, 1,
               1, 0, 0, 0, 0, 0, 0, 1],
              
              [0, 1, 1, 1, 1, 1, 1, 0,  # 'Е'
               0, 1, 0, 0, 0, 0, 0, 0,
               0, 1, 0, 0, 0, 0, 0, 0,
               0, 1, 1, 1, 1, 1, 1, 0,
               0, 1, 0, 0, 0, 0, 0, 0,
               0, 1, 0, 0, 0, 0, 0, 0,
               0, 1, 1, 1, 1, 1, 1, 0],
              
              [0, 0, 0, 1, 1, 1, 1, 0,  # 'Є'
               0, 0, 1, 0, 0, 0, 0, 0,
               0, 1, 0, 0, 0, 0, 0, 0,
               0, 1, 1, 1, 1, 1, 1, 0,
               0, 1, 0, 0, 0, 0, 0, 0,
               0, 0, 1, 0, 0, 0, 0, 0,
               0, 0, 0, 1, 1, 1, 1, 0],
              
              [1, 0, 0, 1, 1, 0, 0, 1,  # 'Ж'
               0, 1, 0, 1, 1, 0, 1, 0,
               0, 1, 1, 1, 1, 1, 0, 0,
               1, 1, 1, 1, 1, 1, 1, 1,
               0, 0, 1, 1, 1, 1, 0, 0,
               0, 1, 0, 1, 1, 0, 1, 0,
               1, 0, 0, 1, 1, 0, 0, 1],
              
              [0, 1, 1, 1, 1, 1, 0, 0,  # 'З'
               0, 0, 0, 0, 0, 0, 1, 0,
               0, 0, 0, 0, 0, 0, 1, 0,
               0, 1, 1, 1, 1, 1, 1, 0,
               0, 0, 0, 0, 0, 0, 1, 0,
               0, 0, 0, 0, 0, 0, 1, 0,
               0, 1, 1, 1, 1, 1, 0, 0],
     ])

# Вихідні дані (бажані відповіді для кожної букви)
desired_outputs = np.array([[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 'А'
                            [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 'Б'
                            [0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 'В'
                            [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 'Г'
                            [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 'Ґ'
                            [0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 'Д'
                            [0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 'Е'
                            [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 'Є'
                            [0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 'Ж'
                            [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # 'З'
         ])  

# Ініціалізація вагових коефіцієнтів зі зміненою розмірністю
np.random.seed(1)
synaptic_weights = 0.01 * np.random.randn(56, 33)  # Змінена розмірність вагових коефіцієнтів і використання нормального розподілу

# Коефіцієнт швидкості навчання
learning_rate = 0.01

# Кількість ітерацій для навчання (збільшена кількість ітерацій)
epochs = 500

# Лічильник для кількості ітерацій
iteration_counter = 0

# Навчання персептрона
for epoch in range(epochs):
    for i in range(len(X)):
        # Прямий прохід
        input_layer = X[i]
        output = np.dot(input_layer, synaptic_weights) # скалярний добуток вхідних даних та вагових коефіцієнтів
        
        # Визначення активації (поріг)
        activation = (output > 0).astype(int) # Якщо вихід більший за 0, нейрон активується (видає 1), в іншому випадку - неактивний (видає 0)
        
        # Різниця між бажаним виходом і фактичним виходом
        error = desired_outputs[i] - activation
        
        # Оновлення вагових коефіцієнтів і нейронного зміщення
        delta_weights = learning_rate * np.outer(input_layer, error) #добуток швидкості навчання на зовнішній добуток вхідних даних та помилки
        synaptic_weights += delta_weights

        # Інкрементуємо лічильник ітерацій
        iteration_counter += 1

    # Якщо мережа досягла великої точності, можна завершити навчання раніше
    if np.mean(np.abs(error)) < 0.01:
        print(f"Training is complete after  {iteration_counter} iteration")
        break

# Функція для розпізнавання букви та виводу відповідних даних
def recognize_letter(letter):
    if letter in 'АБВГҐДЕЄЖЗ':
        letter_index = ord(letter) - ord('А')  # Індекс букви у матриці
        input_test = X[letter_index] # витягуємо вектор вхідних даних з матриці X
        output_test = np.dot(input_test, synaptic_weights) # скалярний добуток вхідних даних та вагових коефіцієнтів
        weights_for_letter = synaptic_weights[:, letter_index]# вагові коефіцієнти для цієї букви
        bias_for_letter = synaptic_weights[-1, letter_index]  # Останній рядок - нейронне зміщення


        activation = output_test > 0
        # Результат визначення активації буде містити 1, якщо нейрон активний, та 0, якщо нейрон неактивний.
        # Округлюємо вихід та ваги до 3 знаків після коми
        weights_rounded = np.round(weights_for_letter, 3)
        bias_rounded = np.round(bias_for_letter, 3)

        print(f"Letter {letter}:")
        print("Exit:")
        print(activation.astype(int))
        print("Weights:")
        print(weights_rounded)
        print("Bias:")
        print(bias_rounded)
    else:
        print("The letter is not recognized. Enter one of the letters АБВГҐДЕЄЖЗ.")

# Введення користувача
user_input = input("Enter one letter: ")
recognize_letter(user_input.upper())  # Перетворення на великі літери