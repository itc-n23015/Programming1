import pickle
sample_num = 100
with open('sample.pkl','wb') as f:
    pickle.dump(sample_num, f)


import pickle
with open('sample.pkl','rb') as f:
    load_num = pickle.load(f)
    print(load_num)
