
""" Convert dollar into yen and return"""
def convert_dollar_yen(dollar):
    yen_rate = 146.67
    yen = []
    
    for i in dollar:
        convert = i * yen_rate
        yen.append(convert)
        
    return yen


""" Convert dollar into peso and return"""
def convert_dollar_peso(dollar):
    peso_rate = 57.17
    peso = []
    
    for i in dollar:
        convert = i * peso_rate
        peso.append(convert)
        
    return peso


def main():
    dollar_yen = []
    dollar_peso = []
    currency_text = ["Dollar($)", "Phil Peso(P)", "Jpn Yen (Y)"]
    
    dollar = input("Enter currency ($): ").split(",")
    
    for i in range(len(dollar)):
        dollar[i] = float(dollar[i])
        
    dollar_peso = convert_dollar_peso(dollar)
    dollar_yen = convert_dollar_yen(dollar)
    
    
    for currency in currency_text:
        print(f"{currency:<15}", end='')
    print()
    
    for i in range(len(dollar)):
        print(f"{dollar[i]:<15.0f} {dollar_peso[i]:<15.2f} {dollar_yen[i]:<15.2f}")
        
    
main()
    
    