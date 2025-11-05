import pickle
talaba1 = {'ism':'Hasan', 'kurs':3, 'fakultet':'informatika'}
talaba2 = {'ism':'Olim', 'kurs':2, 'fakultet':'matematika'}

with open('info123.txt','wb') as file:
    pickle.dump(talaba1,file)
    pickle.dump(talaba2,file)