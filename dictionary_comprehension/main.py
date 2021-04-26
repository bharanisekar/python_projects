# sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
#
# li = list(sentence.split(" "))
# result={l:len(l) for l in li }
# print(result)
# # for i in li:
# #     d = {
# #         f"{i}": len(i)
# #     }
# #     print(d)

weather_c = {
    "days":["monday", "tuesday"],
    "temop":[22, 56]
}

# weather_f ={k:(v*9/5 +32) for (k,v) in weather_c.items()}
#
# print(weather_f)
import pandas

data = pandas.DataFrame(weather_c)
for (index,row) in data.iterrows():
    print(row.days)


# print(result)