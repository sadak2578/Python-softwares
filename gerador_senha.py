import random
import string

keys_list = [
    'Irlandadonorte','Valfenda','','Lancelot','Hambster','Navarro', 'Adventure','Watermelon','Enchantment','Revolution','Connection','Confidence','Recreation',
    'Leadership','Commitment','Forgiveness','Awareness','Excitement','Elevation','Exploration','Protection','Motivation','Reflection','Mastermind','Brightness','Difference','Overcoming','RadiantSky',
    'Transformation','Stargazing'


]  
symbols_for_pass = ['!','@','*']
numbers = ['1','2','3','4','5','6','7','8','9','10','99','28','76','23','1']
def results(tamanho=21):
    random_item = random.choice([item for item in keys_list if item])
    random_item_symbol = random.choice(symbols_for_pass)
    random_numbers = random.choice(numbers)
    result = random_item + random_item_symbol + random_numbers
    
    others_caracters = tamanho - len(result)
    
    if others_caracters > 0:
        result += ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(others_caracters))
        
    print('senha gerada: ', result)

results()
