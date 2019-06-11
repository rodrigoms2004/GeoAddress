import pandas as pd
from queryGoogle import queryAddress


def generateResult(filename, columnName):

    addressFile = filename
    df_linhas = pd.read_excel(addressFile, sheet_name = 0)

    # lista vazia
    row_list = []

    for index, value in df_linhas.iterrows() : 

        address = str(value[columnName]) + ", São Paulo"

        if address != 'nan':
            queryTuple = queryAddress(address.replace(' ', '+'))

            try:
                address_dictionary = {}
                address_dictionary['Endereco']  = address

                if (len(queryTuple) == 3):
                    address_dictionary['query']     = "ok"
                    address_dictionary['CEP']       = queryTuple[0]
                    address_dictionary['latitude']  = queryTuple[1]
                    address_dictionary['longitude'] = queryTuple[2]
                else:
                    address_dictionary['query']     = "não encontrado"

                print(address_dictionary)

                row_list.append(address_dictionary)

            except ValueError as ve:
                print(ve)
            except:
                print("error")

        df_result = pd.DataFrame(row_list)

        result_file = "result_" + columnName + ".xlsx"

        # df_result.to_excel(result_file, columnName, '', None, None, True)
        df_result.to_excel(result_file, columnName)


filename = 'CUSTOMER_.xlsx'
generateResult(filename, 'LINHA1')
generateResult(filename, 'LINHA2')
generateResult(filename, 'LINHA3')



