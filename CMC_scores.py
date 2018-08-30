import numpy as np

predictions = np.random.randint(10, size=(100,20))
labels = np.random.randint(10,size=100)

print predictions
print labels

ranks = np.zeros(len(labels))

for i in range(len(labels)) :
    if labels[i] in predictions[i] :
        firstOccurance = np.argmax(predictions[i]== labels[i])        
        for j in range(firstOccurance, len(labels)) :            
            ranks[j] +=1

print ranks
cmcScores = [float(i)/float(len(labels)) for i in ranks]
print cmcScores

