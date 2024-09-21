def temperature_statistics(T):
    n = len(T)
    mean_T = sum(T)/n
    std = 0

    for i in range(0, n):
        std += (T[i] - mean_T)**2
    
    std_final = (std/n)**0.5

    return "Average temperature : ", mean_T, "Temperaure standard deviation", std_final

temp_list = [17.2, 22, 26.3, 28.4, 28.8, 29, 28.7, 28.9, 28.5, 27.4, 24, 20]
temp_list_2 = [-13.9,-11.4,-4.9,5.2,11.8,16.1,19,18.2,12,4.4,-5.2,-12.4]
