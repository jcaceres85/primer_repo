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
    pass



def get_guessed_word(secret_word, letters_guessed):
    '''
    secret_word: string, la palabra que el usuario está adivinando
     letters_guessed: list (of letters), que letras han sido adivinadas hasta el momento
     returns: cadena, compuesta de letras, guiones bajos (_) y espacios que representan
       qué letras en secret_word se han adivinado hasta ahora.
    '''
    # LLENA TU CÓDIGO AQUÍ Y ELIMINA "pass"
    pass



def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of letters), que letras han sido adivinadas hasta el momento
     devuelve: string (de letras), compuesta de letras que representa qué letras no
       han sido adivinadas.
    '''
    # LLENA TU CÓDIGO AQUÍ Y ELIMINA "pase"
    pass
    
    

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
    pass



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
    pass



def show_possible_matches(my_word):
    '''
    my_word: string con _ caracteres, intento actual de palabra secreta
     returns: nada, pero debería imprimir cada palabra en la lista de palabras que coincida con my_word
              Tenga en cuenta que en hangman cuando se adivina una letra, todas las posiciones
              en las que aparece esa letra en la palabra secreta se revelan.
              Por lo tanto, la letra oculta (_) no puede ser una de las letras de la palabra
              que ya ha sido revelada.
    
    '''
    # LLENA TU CÓDIGO AQUÍ Y ELIMINA "pass"
    pass



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
    pass



# Cuando haya completado su función hangman_with_hint, comente las dos lineas
# similares arriba que se usaron para ejecutar la función del ahorcado, y luego descomente
# las siguentes dos líneas y ejecute este archivo para probar!
# Sugerencia: es posible que desee elegir su propia palabra secreta mientras realiza la prueba.

if __name__ == "__main__":
     pass

    # Para probar la parte 2, comente la línea de pass de arriba y
#     descomentar las siguientes dos líneas.
    
#    secret_word = choose_word(wordlist)
#    hangman(secret_word)

###############
    
    # Para probar la parte 3 vuelve a comentar las líneas anteriores y
#     descomentar las siguientes dos líneas. 
    
    #secret_word = choose_word(wordlist)
    #hangman_with_hints(secret_word)
