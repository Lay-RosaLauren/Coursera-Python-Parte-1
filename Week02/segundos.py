segundos_str = input("Por favor, entre com o número de segundos que deseja converter: ")
total_segs = int(segundos_str)

dias = total_segs // (3600 * 24)
segs_restantes1 = total_segs % (3600 * 24)

horas = segs_restantes1 // 3600                    # a quantidade de horas é a divisão inteira (3600s = 1h)
segs_restantes2 = segs_restantes1 % 3600           # o resto da divisão são os segundos restantes

minutos =segs_restantes2 // 60                     # os minutos são os segundos restantes acima dividido por 60 (60s = 1 min)
segs_restantes_final = segs_restantes2 % 60        # os segundos finais é o resto de segs_restantes por 60

print(dias, "dias,",horas, "horas,",minutos, "minutos e",segs_restantes_final, "segundos.")
