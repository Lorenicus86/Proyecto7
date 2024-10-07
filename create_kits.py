import sender_stand_request
import data

    # Función de prueba positiva
def positive_assert(name):
    # El cuerpo de la solicitud actualizada se guarda en la variable kit_body
    kit_body = get_kit_body(name)
    # El resultado de la solicitud se guarda en la variable user_response
    user_response = sender_stand_request.post_new_kit(kit_body)

    # Comprueba si el código de estado es 201
    assert user_response.status_code == 201
    # Comprueba que el campo authToken está en la respuesta y contiene un valor
    assert user_response.json()["authToken"] != ""

    # El resultado de la solicitud de recepción de datos de la tabla "user_model" se guarda en la variable "users_table_response"
    users_table_response = sender_stand_request.get_users_table()

    # String que debe estar en el cuerpo de respuesta
    str_user = kit_body["name"] + user_response.json()["authToken"]

    # Comprueba si el usuario o usuaria existe y es único/a
    assert users_table_response.text.count(str_user) == 1


def negative_assert_symbol(name):
    # El cuerpo actualizado de la solicitud se guarda en la variable kit_body
    kit_body = get_kit_body(name)

    # El resultado se guarda en la variable response
    response = sender_stand_request.post_new_kit(kit_body)

    # Comprueba si el código de estado es 400
    assert response.status_code == 400

    # Comprueba que el atributo code en el cuerpo de respuesta es 400
    assert response.json()["code"] == 400
    # Comprueba el atributo message en el cuerpo de respuesta
    assert response.json()["message"] == "El nombre que ingresaste es incorrecto. " \
                                         "El número de caracteres es mayor que la cantidad permitida (512)"

def create_kit_1_letter_in_name_get_success_response():
    positive_assert("a")

def create_kit_menos_de_511_letters_in_name_get_success_response():
    positive_assert("El valor de prueba para esta comprobación será inferior a")

def create_kit_menos_de_1_letter_in_name_get_error_response():
    negative_assert_symbol("")

def create_kit_mas_de_511_letters_in_name_get_error_response():
    negative_assert_symbol("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

def create_kit_caracter_special_in_name_get_error_response():
    negative_assert_symbol("%@"")

def create_kit_spacies_in_name_get_error_response():
    negative_assert_symbol(" A Aaa")

def create_kit_numbers_in_name_get_error_response():
    negative_assert_symbol("123")

def create_kit_sin_parameter_in_name_get_error_response():
    negative_assert_symbol()

def create_kit_different_parameter_in_name_get_error_response():
    negative_assert_symbol(123)


