import random
import pandas as pd
import seaborn as sns
import matplotlib
import ast

matplotlib.use("TkAgg")
import matplotlib.pyplot as plt

def uploaddoc():
    doc_o = pd.read_csv("./iris.csv")
    doc_o.drop(columns=["sepal.length", "sepal.width"], inplace=True)
    #doc_o.drop_duplicates(subset=["petal.width", "petal.length", "variety"], inplace=True)
    return doc_o, (doc_o["petal.length"].max() + 1, doc_o["petal.width"].max() + 1)

def showdoc(df_original, df_new=None):

    df_original = pd.concat([df_original, df_new], ignore_index=True)
    sns.scatterplot(
        data=df_original,
        x="petal.width",
        y="petal.length",
        hue="variety",
        s=30,
        palette="Set1"
    )

    plt.xlabel("Petal Width")
    plt.ylabel("Petal Length")
    plt.title("Iris Dataset con Nuevos Puntos Clasificados")
    plt.legend(loc="upper left")
    plt.show()

def compute_centroid(parameter, criteria):
    c = list()
    for x in range(0, parameter):
        c.append([float(random.uniform(0,criteria[0])),
                  float(random.uniform(0,criteria[1])),
                  "Class{}".format(x)])
    return pd.DataFrame(c, columns=["petal.length", "petal.width", "variety"])

def get_parameters(criteria):
    i = int(input("Proporciona el paremetro 'k': "))
    return i, compute_centroid(i, criteria)

def compute_average(doc_o):
    # 0 index 1 length 2 width 3 variety
    # new_centroid: 0 length 1 width 2 no.dots
    new_centroid = dict()
    aux_c = list()
    for dot_o in doc_o.itertuples():
        aux = ast.literal_eval(dot_o[3])
        for cl in aux:
            if cl in new_centroid:
                new_centroid[cl][0] += dot_o[1]
                new_centroid[cl][1] += dot_o[2]
                new_centroid[cl][2] += 1
            else:
                new_centroid[cl]= [0,0,0]
                new_centroid[cl][0] += dot_o[1]
                new_centroid[cl][1] += dot_o[2]
                new_centroid[cl][2] += 1

    for element in new_centroid:
        l = new_centroid[element][0] / new_centroid[element][2]
        w = new_centroid[element][1] / new_centroid[element][2]
        v = element
        aux_c.append([l, w, v])

    return pd.DataFrame(aux_c, columns=["petal.length", "petal.width", "variety"])

def compute_distance(o_dots, c_dots):
    flag = False
    for dot_o in o_dots.itertuples():
        # 0 index 1 length 2 width 3 variety
        aux_distance = dict()
        for c_dot in c_dots.itertuples():
            dif_l = dot_o[1] - c_dot[1]
            dif_w = dot_o[2] - c_dot[2]
            distance = (dif_l ** 2 + dif_w ** 2) ** 0.5
            # distance = round(distance, 2)
            aux_distance[c_dot[3]] = distance
        min_val = min(aux_distance.values())
        keys_min = [k for k, v in aux_distance.items() if v == min_val]
        # print(str(dot_o[3]), "-->" ,str(keys_min))
        if not flag:
            # print("Acceso a if")
            if str(dot_o[3]) != str(keys_min):
                flag = True
        o_dots.loc[dot_o.Index, 'variety'] = str(keys_min)
        # print(flag)
    # x = input("----------------------------------")
    return o_dots, flag

if __name__ == '__main__':
    doc, cri = uploaddoc()
    par, cen = get_parameters(cri)
    fg = True
    while fg:
        doc, fg = compute_distance(doc, cen)
        cen = compute_average(doc)
    showdoc(doc)