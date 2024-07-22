def caching_fibonacci():
  
    # Створюємо словник для кешування результатів
    cache = {}
    
    def fibonacci(n):
   
        # Базові випадки
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        
        # Перевіряємо, чи є результат у кеші
        if n in cache:
            return cache[n]
        
        # Якщо результату немає в кеші, обчислюємо його
        result = fibonacci(n - 1) + fibonacci(n - 2)
        
        # Зберігаємо результат у кеші
        cache[n] = result
        
        return result
    
    return fibonacci

