# Problema de Aplicación 2, hangman.py
# Nombre: 
# Colaboradores:
# Tiempo invertido:

# Hangman Game
# -----------------------------------
# Código de ayuda
# No es necesario que entiendas este código de ayuda,
# pero deberás saber cómo usar las funciones
# (¡así que asegúrese de leer los docstrings!)
import random
import string

WORDLIST_FILENAME = "palabras.txt"


def load_words():
    """
    Devuelve una lista de palabras válidas. Las palabras son cadenas de letras minúsculas.
    
    Dependiendo del tamaño de la lista de palabras, esta función puede
    tomar un tiempo en terminar.
    """
    print("Cargando lista de palabras desde archivo...")
    # inFile: Abrir archivo
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: cadena
    line = inFile.readlines()
#    line = [line.rstrip('\n') for line in inFile] #Esto es el equivalente a la linea anterior
#    print(line)
    line_string = ' '.join(line)
#    print(line_string)
    # wordlist: lista de cadenas
    wordlist = line_string.split()
    print("  ", len(wordlist), "palabras cargadas.")
    return wordlist



def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Devuelve una palabra de la lista de palabras al azar
    """
    return random.choice(wordlist)

# fin del código de ayuda

# -----------------------------------

# Cargar la lista de palabras en la variable wordlist
# para que se pueda acceder desde cualquier lugar del programa
wordlist = load_words()


def is_word_guessed(secret_word, letters_guessed):
    '''
    secret_word: string, la palabra que el usuario está adivinando; asume que todas las letras son
       minúsculas
     letters_guessed: list (de letras), que letras han sido adivinadas hasta el momento;
       asume que todas las letras son minúsculas
     returns: boolean, True si todas las letras de secret_word están en letters_guessed;
       False de lo contrario
    '''
    # LLENA TU CÓDIGO AQUÍ Y ELIMINA "pass"
    #Por cada letra en secret_word, si la letra no está en letters_guessed
    #entonces el intento es falso
#    for char in secret_word:
#      if (char in letters_guessed) == False:
#        guessed = False
#        break
#      else:
#        guessed = True
#    
#    return guessed

    #Metodo alternativo
    for char in secret_word:
        if char not in letters_guessed:
            return False
        
    return True
            



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, la palabra que el usuario está adivinando
     letters_guessed: list (of letters), que letras han sido adivinadas hasta el momento
     returns: cadena, compuesta de letras, guiones bajos (_) y espacios que representan
       qué letras en secret_word se han adivinado hasta ahora.
    '''
    # LLENA TU CÓDIGO AQUÍ Y ELIMINA "pass"
    #Cree una variable tipo lista vacía donde almacenará las letras correctas
    #Llamele a esta variable correct_letters
    correct_letters = []
    
    #Cree una variable tipo cadena vacía donde almacenará la cadena adivinada
    #Llamele a esta variable guessed_string
    guessed_string = ""
    
    # cree un for loop para tomar cada letra dentro de letters_guessed
    # si una letra adivinada está en la palabra secreta,
    # almacene esa letra en la lista de correct_letters
    for char in letters_guessed:
        if char in secret_word:
            correct_letters.append(char)

    #por cada letra en secret_word, que ya ha sido adivinada,
    #agreguela en la guessed_strings, de lo contrario, aguregue "_ "
    for char in secret_word:
        if char in correct_letters:
            guessed_string += char
        else:
            guessed_string += '_ '
    
    #regrese guessed_string        
    return guessed_string


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), que letras han sido adivinadas hasta el momento
     devuelve: string (de letras), compuesta de letras que representa qué letras no
       han sido adivinadas.
    '''
    # LLENA TU CÓDIGO AQUÍ Y ELIMINA "pase"
    
    #primero obtenga todas las letras disponibles en minúsculas
    #Utilize la función sugerida en el guión de prácticas, llamele a la variable
    #letters
    letters = string.ascii_lowercase
    
    #Cree una variable de cadena vacía para almacenar las letras que no han sido
    #adivinadas. Llamele unguessed
    unguessed = ""
    
    #para cada elemento en letters, verifique si ha sido adivinado;
    #si no, agreguelo a variable unguessed
    for char in letters:
        if char not in letters_guessed:
            unguessed += char
    
    #regrese unguessed
    return unguessed
    
##############################################################################
##############################################################################
#ESTO NO ES PARTE DEL ARCHIVO ORIGINAL  

#Cree una función para revisar las advertencias faltantes    
def check_warnings(warnings_remaining, user_guess, duplicate_guesses, display):
    '''
    1. Esta función debe comenzar restando 1 a la variable warnings_remaining.
    2. Luego debe evaluar si el user_guess no isalpha(). Deberá imprimir un texto si la letra
    ingresada no es válida y deberá decirle cuantas advertencias le quedan.
    3. Deberá tambien evaluar, dentro de la misma cadena de condicionales, si el user_guess
    ya está en duplicate_guess y deberá indicarle al usuario que ya ha intentado esa letra
    y deberá decirle cuantas advertencias le quedan
    '''
    warnings_remaining -= 1
    #declaración print diferente dependiendo de si el usuario
    #ingresó una entrada no válida o una letra repetida
    if not user_guess.isalpha():
        print('Oops! Esa no es una letra válida. Te quedan {} advertencias: {}'.format(warnings_remaining, display))
    elif user_guess in duplicate_guesses:
        print('Oops! Ya has intentado esa letra. Te quedan {} advertencias: {}'.format(warnings_remaining, display))
    print("----------------------")
    return warnings_remaining

#Cree una función para comprobar cuantos intentos quedan
def check_guesses(guesses_remaining, user_guess, duplicate_guesses, display):
    '''
    1. Esta función debe comenzar restando 1 a la variable guesses_remaining.
    2. Luego debe evaluar si el user_guess no isalpha() y si el carácter introducido no es un '*'.
    Deberá imprimir un texto indicandole al usuario que la letra no es válida y que no le quedan
    más advertenciass, por lo cual le indicará que perderá un intento.
    3. Deberá tambien evaluar, dentro de la misma cadena de condicionales, si el user_guess
    ya está en duplicate_guess y deberá indicarle al usuario que ya ha intentado esa letra
    y que no le quedan más advertenciass, por lo cual le indicará que perderá un intento
    4. En caso que ninguna de las condiciones anteriores se hayan cumplido, deberá imprimir un texto
    diciendole al usuario que la letra que ha ingresado no forma parte de la palabra y deberá mostrar
    la palabra adivinada hasta el momento.
    '''
    guesses_remaining -= 1
    #declaración print diferente dependiendo de si el usuario
    #ingresó una entrada no válida o una letra repetida
    #Evalua también si el usuario ingresó un '*' ya que esto deberá considerarse un intento válido para la parte 3
    if not user_guess.isalpha() and user_guess != '*':
        print('Oops! Esa no es una letra válida. No tienes más advertencias, así que pierdes un intento: {}'.format(display))
    elif user_guess in duplicate_guesses:
        print('Oops! Ya has intentado esa letra. No tienes más advertencias, así que pierdes un intento: {}'.format(display))
    else:
        print('Oops! Esa letra no está en mi palabra: {}'.format(display))
    print("----------------------")
    return guesses_remaining

##############################################################################
##############################################################################

def hangman(secret_word):
    '''
    secret_word: string, la palabra secreta para adivinar.
    
     Inicia un juego interactivo de Ahorcado.
    
     * Al comienzo del juego, deje que el usuario sepa cuántos
       letras la secret_word contiene y con cuántos intentos comienza.
      
     * El usuario debe comenzar con 6 intentos

     * Antes de cada ronda, debe mostrar al usuario la cantidad de intentos
       que tiene y las letras que el usuario aún no ha adivinado.
    
     * Pídale al usuario que proporcione un intento por ronda. Recuerde asegurarte
       que el usuario ponga una letra!
    
     * El usuario debe recibir comentarios inmediatamente después de cada intento
       sobre si su intento aparece en la palabra de la computadora.

     * Después de cada intento, debe mostrar al usuario la
       palabra parcialmente adivinada hasta ahora.
    
     Sigue las otras limitaciones detalladas en la descripción del problema.
    
    '''
    # LLENA TU CÓDIGO AQUÍ Y ELIMINA "pass"
    #Crear una lista vacía y llamarla letters_guessed, la cual almacenará las letras
    #ingresadas por el usuario    
    letters_guessed = []
    #Crear una lista vacía y llamarla duplicate_guessed, la cual rasterará si se ha
    #ingresado la misma letra dos veces
    duplicate_guesses = []
    #Inicializar la variable guesses_remaining con la cantidad de intentos disponibles
    guesses_remaining = 6
    #Inicializar la variable warnings_remaining con la cantidad de advertencias disponibles
    warnings_remaining = 3
    
    #display para mostrar la cadena adivinada - inicializar el espacio en
    #blanco para que las letras que se adivinan la primera vez (no repetir)
    #no sean consideradas repeticiones
    display = '_ ' * (len(secret_word))
#    display = get_guessed_word(secret_word, letters_guessed)
    
    #Calcular el número de letras únicas en la palabra en secret_word
    #inicializar una cadena vacía y llamele unique_letters
    unique_letters = ''
    for letter in secret_word:
        if letter not in unique_letters:
            unique_letters += letter
    
    #De la bienvenida al programa, tal y como está en el guión de prácticas    
    print('Bienvenido al juego de Ahorcados!')
    print('Estoy pensando en una palabra que tiene {} letras'.format(len(secret_word)))
    print('---------------------')
    print('Tienes {} advertencias restantes'.format(warnings_remaining))
    
    #while True:
    while True:
        letters_left = get_available_letters(letters_guessed)
        print('Tienes {} intentos restantes'.format(guesses_remaining))
        print('Letras disponibles: {}'.format(letters_left))
        
        #Pide al usuario su input y conviertela en minúsculas
        user_guess = (input("Por favor ingresa una letra: ")).lower()
        
        #Verifica lo que el usuario ingresó
        if not user_guess.isalpha():
            #si el usuario no ingresó una letra, primero reduzca las
            #advertencias; si no hay advertencias, reduce los intentos
            if warnings_remaining > 0:
                warnings_remaining = check_warnings(warnings_remaining, user_guess, duplicate_guesses, display)
            elif guesses_remaining > 1:
                guesses_remaining = check_guesses(guesses_remaining, user_guess, duplicate_guesses, display)
            else:
                print("Lo siento, se te acabaron los intentos. La palabra era ‘{}’".format(secret_word))
                break
        #El siguiente código se ejecuta si el usuario ingresó una letra válida
        else:
            #agrega el intento a letters_guessed
            if user_guess not in letters_guessed:
                letters_guessed.append(user_guess)
            #comprueba si el usuario adivinó todas las letras correctas
            #llamale a la variable game_over y asignale el valor que resulte de la función
            #is_word_guessed(secret_word, letters_guessed)
            game_over = is_word_guessed(secret_word, letters_guessed)
            
            #salir del loop si game_over es verdadero (todas las letras
            #se adivinan correctamente)
            if game_over:
                display = get_guessed_word(secret_word, letters_guessed)
                print('Buen intento: {}'.format(display))
                print('----------------------')
                print("¡Felicitaciones, has ganado!")
                total_score = guesses_remaining * len(unique_letters)
                print('Tu puntaje total para este juego es: {}'.format(total_score))
                break
            #De lo contrario, compruebe si el intento ya se ha adivinado
            elif user_guess in duplicate_guesses:
                if warnings_remaining > 0:
                    warnings_remaining = check_warnings(warnings_remaining, user_guess, duplicate_guesses, display)
                elif guesses_remaining > 1:
                    guesses_remaining = check_guesses(guesses_remaining, user_guess, duplicate_guesses, display)
            #Si no, comprueba si el intento está en la palabra; si es verdad
            elif (not (user_guess in duplicate_guesses)) and user_guess in secret_word:
                display = get_guessed_word(secret_word, letters_guessed)
                print('Buen intento: {}'.format(display))
                print('----------------------')
            #De lo contrario, compruebe si el intento está en la palabra; if false:
            elif user_guess not in secret_word:
                if user_guess in ['a', 'e', 'i', 'o', 'u'] and guesses_remaining > 1:
                    #menos 2 intentos si es una vocal, pero la función check_guesses
                    #también resta un intento, por lo cual solo restar 1
                    guesses_remaining = guesses_remaining - 1
                    guesses_remaining = check_guesses(guesses_remaining, user_guess, duplicate_guesses, display)
                elif guesses_remaining > 1:
                    guesses_remaining = check_guesses(guesses_remaining, user_guess, duplicate_guesses, display)
                else:
                    print('Oops! Esa letra no está en mi palabra: {}'.format(display))
                    print("----------------------")
                    print('Lo siento, se te acabaron los intentos. La palabra era ‘{}’'.format(secret_word))
                    break
                
        duplicate_guesses.append(user_guess)
            

# Cuando hayas completado tu función de ahorcado, desplázate hacia abajo
# del archivo y descomenta las primeras dos líneas para probarlo
# (sugerencia: es posible que desee elegir su propio
# secret_word mientras haces tus propias pruebas)


# -----------------------------------



def match_with_gaps(my_word, other_word):
    '''
    my_word: string con _ caracteres, intento actual de palabra secreta
     other_word: string, palabra regular en español
     returns: boolean, True si todas las letras reales de my_word coinciden con
         letras correspondientes de other_word, o la letra es el símbolo especial
         _, y my_word y other_word son de la misma longitud;
         False de lo contrario:
    '''
    # LLENA TU CÓDIGO AQUÍ Y ELIMINA "pass"
    
    #Crear una variable de tipo cadena, vacía, para almacenar la palabra faltante
    #sin espacios, llamele my_word_no_space
    my_word_no_space = ''
    
    #Cree una variable de tipo lista, vacía, para almacenar las letras faltantes
    #dentro de la palabra, llamele guessd_letters
    guessed_letters = []
    
    #Utilice un for loop para extraer cada letra de my_word
    for char in my_word:
        #Si la letra no es un espacio vacío, entonces agrege la letra
        #a la cadena my_word_no_space
        if char != ' ':
            my_word_no_space += char
        
        #Si la letra es una letra válida (isalpha), entonces adjunte la letra
        #a la lista guessed_letters
        if char.isalpha():
            guessed_letters.append(char)
    
    #Si la longitud de my_word_no_space es diferente a la longitud de other word
    #regrese el valor False directamente. Considere utilizar la funcion
    #my_word_no_space.strip() y other_word.strip()
    if len(my_word_no_space.strip()) != len(other_word.strip()):
        return False
    
    #Cree un for loop utilizando un range, defina el parámetro stop del range
    #como la longitud de la palabra my_word_no_space
    for i in range(len(my_word_no_space)):
        #Cree una variable para almacena la letra de my_word_no_space en la primera
        #posición. Al ser un for loop esta variable va a ir tomando el valor de cada
        #letra en my_word_no_space. LLamele a esta variable current_letter
        current_letter = my_word_no_space[i]
        
        #Al igual que el anterior. Cree una variable que tome el valor de cada
        #letra en other_word. Llamele a esta variable other_letter
        other_letter = other_word[i]
        
        #Si current_letter isalpha():
        if current_letter.isalpha():
            #Si current_letter es distinto de other_letter:
            if current_letter != other_letter:
                #Regrese False
                return False
        
        #Caso contratio:
        else:
            #Si current_letter es igual a '_' y other_letter está en guessed_letters:
            if current_letter == '_' and other_letter in guessed_letters:
                #Regrese False
                return False
            
    #Regrese True
    return True
            



def show_possible_matches(my_word):
    '''
    my_word: string con _ caracteres, intento actual de palabra secreta
     returns: None, pero debería imprimir cada palabra en la lista de palabras que coincida con my_word
              Tenga en cuenta que en hangman cuando se adivina una letra, todas las posiciones
              en las que aparece esa letra en la palabra secreta se revelan.
              Por lo tanto, la letra oculta (_) no puede ser una de las letras de la palabra
              que ya ha sido revelada.
    
    '''
    # LLENA TU CÓDIGO AQUÍ Y ELIMINA "pass"
    #Cree variable de tipo lista vacía, para almacenar todas las posibles
    #palabras que sean coincidentes. LLamele a la variable matched_words
    matched_words = []
    
    #Utilizar un foor loop para iterar en cada palabra dentro de la variable wordlist
    for word in wordlist:
        #Crear un condicional donde se evalue la función match_with_gaps
        #la cual tomará como palámetros my_word y cada palabra dentro de wordlist
        #o sea la variable que se haya creado dentro del for loop
        if match_with_gaps(my_word, word):
            #Adjunte la palabra del for loop dentro de la variable matched_words
            matched_words.append(word)
            
    #Si la longitud de matched_words es mayor que 0
    if len(matched_words) > 0:
        #Utilice un for loop para tomar cada palabra en matched_words
        for word in matched_words:
            #Imprima la variable del for loop
            print(word)
        print()
    #Caso contrario
    else:
        #Imprima 'No se encontraron coincidencias'
        print('No se encontraron coincidencias')



def hangman_with_hints(secret_word):
    '''
    secret_word: string, la palabra secreta para adivinar.
    
     Inicia un juego interactivo de Ahorcado.
    
     * Al comienzo del juego, deje que el usuario sepa cuántos
       letras contiene la secret_word y con cuántos intentos comienza.
      
     * El usuario debe comenzar con 6 intentos

     * Antes de cada ronda, debe mostrar al usuario la cantidad de intentos
       que tiene y las letras que el usuario aún no ha adivinado.
    
     * Pídale al usuario que proporcione un intento por ronda. Recuerde asegurarte
       que el usuario ponga una letra!
    
     * El usuario debe recibir comentarios inmediatamente después de cada intento
       sobre si su intento aparece en la palabra de la computadora.

     * Después de cada intento, debe mostrar al usuario la
       palabra parcialmente adivinada hasta ahora.
      
     * Si el intento es el símbolo *, imprima todas las palabras en wordlist que
       coincide con la palabra actual adivinada.
    
     Sigue las otras limitaciones detalladas en la descripción del problema.
    
    '''
    # LLENA TU CÓDIGO AQUÍ Y ELIMINA "pass"
    #Crear una lista vacía y llamarla letters_guessed, la cual almacenará las letras
    #ingresadas por el usuario
    letters_guessed = []
    #Crear una lista vacía y llamarla duplicate_guessed, la cual rasterará si se ha
    #ingresado la misma letra dos veces
    duplicate_guesses = [] #utilizado para rastrear cualquier duplicate_guesses
    #Inicializar la variable guesses_remaining con la cantidad de intentos disponibles
    guesses_remaining = 6
    #Inicializar la variable warnings_remaining con la cantidad de advertencias disponibles
    warnings_remaining = 3
    
    #display para mostrar la cadena adivinada - inicializar el espacio en
    #blanco para que las letras que se adivinan la primera vez (no repetir)
    #no sean consideradas repeticiones
    display = '_ ' * (len(secret_word))
#    display = get_guessed_word(secret_word, letters_guessed)
    
    #Calcular el número de letras únicas en la palabra en secret_word
    #inicializar una cadena vacía y llamele unique_letters
    unique_letters = ''
    for letter in secret_word:
        if letter not in unique_letters:
            unique_letters += letter
    
    #De la bienvenida al programa, tal y como está en el guión de prácticas        
    print('Bienvenido al juego de Ahorcados!')
    print('Estoy pensando en una palabra que tiene {} letras'.format(len(secret_word)))
    print('---------------------')
    print('Tienes {} advertencias restantes'.format(warnings_remaining))
    
    #while True:
    while True:
        #Cree una variable llamada letters_left y asignele el resultado de la función
        #get_available_letters(letters_guessed)
        letters_left = get_available_letters(letters_guessed)
        print('Tienes {} intentos restantes'.format(guesses_remaining))
        print('Letras disponibles: {}'.format(letters_left))
        
        #Pide al usuario su input y conviertela en minúsculas
        user_guess = (input("Por favor ingresa una letra: ")).lower()
        
        #Verifica que lo que el usuario ingreo isalpha y que es diferente de '*'
        if not user_guess.isalpha() and user_guess != '*':
            #si el usuario no ingresó una letra, primero reduzca las
            #advertencias; si no hay advertencias, reduce los intentos
            if warnings_remaining > 0:
                warnings_remaining = check_warnings(warnings_remaining, user_guess, duplicate_guesses, display)
            elif guesses_remaining > 1:
                guesses_remaining = check_guesses(guesses_remaining, user_guess, duplicate_guesses, display)
            else:
                print("Lo siento, se te acabaron los intentos. La palabra era ‘{}’".format(secret_word))
                break
        #El siguiente código se ejecuta si el usuario ingresó una letra válida
        else:
            #agrega el intento a letters_guessed
            if user_guess not in letters_guessed:
                letters_guessed.append(user_guess)
            #comprueba si el usuario adivinó todas las letras correctas
            #llamale a la variable game_over y asignale el valor que resulte de la función
            #is_word_guessed(secret_word, letters_guessed)
            game_over = is_word_guessed(secret_word, letters_guessed)
            
            #salir del loop si game_over es verdadero (todas las letras
            #se adivinan correctamente)
            if game_over:
                display = get_guessed_word(secret_word, letters_guessed)
                print('Buen intento: {}'.format(display))
                print('----------------------')
                print("¡Felicitaciones, has ganado!")
                total_score = guesses_remaining * len(unique_letters)
                print('Tu puntaje total para este juego es: {}'.format(total_score))
                break
            #De lo contrario, compruebe si el intento ya se ha adivinado
            elif user_guess in duplicate_guesses:
                if warnings_remaining > 0:
                    warnings_remaining = check_warnings(warnings_remaining, user_guess, duplicate_guesses, display)
                elif guesses_remaining > 1:
                    guesses_remaining = check_guesses(guesses_remaining, user_guess, duplicate_guesses, display)
            #Si no, comprueba si el intento está en la palabra; si es verdad
            elif (not (user_guess in duplicate_guesses)) and user_guess in secret_word:
                display = get_guessed_word(secret_word, letters_guessed)
                print('Buen intento: {}'.format(display))
                print('----------------------')
            #Si el user_guess fue un '*', muestrele todas las posible coincidencias de la palabra
            if user_guess == '*':
                print('Las posibles coincidencias de palabras son:\n')
                show_possible_matches(display)
            #De lo contrario, compruebe si el intento está en la palabra; if false:
            elif user_guess not in secret_word:
                if user_guess in ['a', 'e', 'i', 'o', 'u'] and guesses_remaining > 1:
                    #menos 2 intentos si es una vocal, pero la función check_guesses
                    #también resta un intento, por lo cual solo restar 1
                    guesses_remaining = guesses_remaining - 1
                    guesses_remaining = check_guesses(guesses_remaining, user_guess, duplicate_guesses, display)
                elif guesses_remaining > 1:
                    guesses_remaining = check_guesses(guesses_remaining, user_guess, duplicate_guesses, display)
                else:
                    print('Oops! Esa letra no está en mi palabra: {}'.format(display))
                    print("----------------------")
                    print('Lo siento, se te acabaron los intentos. La palabra era ‘{}’'.format(secret_word))
                    break
        
        #Adjunte el user_guess a la variable duplicate_guesses        
        duplicate_guesses.append(user_guess)



# Cuando haya completado su función hangman_with_hint, comente las dos lineas
# similares arriba que se usaron para ejecutar la función del ahorcado, y luego descomente
# las siguentes dos líneas y ejecute este archivo para probar!
# Sugerencia: es posible que desee elegir su propia palabra secreta mientras realiza la prueba.

#if __name__ == "__main__":
#     pass

    # Para probar la parte 2, comente la línea de pass de arriba y
#     descomentar las siguientes dos líneas.
    
#secret_word = choose_word(wordlist)
#hangman(secret_word)

###############
    
    # Para probar la parte 3 vuelve a comentar las líneas anteriores y
#     descomentar las siguientes dos líneas. 
    
secret_word = choose_word(wordlist)
hangman_with_hints(secret_word)
