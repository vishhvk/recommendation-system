#importing matplotlib to draw pie charts
import matplotlib.pyplot as plt
#importing the naive bayes algorithm
from naive_bayes import NaiveBayes
#importing the training file.
training_file  = open(&quot;training.txt&quot;, mode= &#39;r&#39;)
training_reviews = training_file.read().split(&quot;.&quot;)
training_reviews.pop(len(training_reviews)-1)
#initializing the training samples
train_x = []
train_y = []
#getting the training samples  (train_x and train_y) from training reveiws
for i in range(len(training_reviews)):
    str = &#39;&#39;
    value = training_reviews[i].split(&#39; &#39;)
    train_x.append(value[0])
    value.pop(0)
    for j in range(len(value)):
        str = str + &#39; &#39; + value[j]
    train_y.append(str)


#importing the testing file
testing_file  = open(&quot;testing.txt&quot;, mode= &#39;r&#39;)
testing_reviews = testing_file.read().split(&#39;.&#39;)
testing_reviews.pop(len(testing_reviews)-1)
#initializing the testing samples
test_x = []
test_y = []
#getting the testing samples (test_x and test_y) from testing reviews.
for i in range(len(testing_reviews)):
    str = &#39;&#39;
    value = testing_reviews[i].split(&#39; &#39;)
    test_x.append(value[0])
    value.pop(0)
    for j in range(len(value)):
        str = str + &#39; &#39; + value[j]
    test_y.append(str)
#creating the naive bayes model
model = NaiveBayes()
#training the model
model.fit(train_x,train_y)
#testing the model
score_calc = model.predict(test_x,test_y)


#score calculation
sum = 0
total = len(score_calc)
for elem in score_calc:
    sum+=elem
percentage = (sum / total) * 100
if(percentage &gt; 100):
    percentage = 100.0
  print(percentage)
#visualising in chart
items = [&#39;Recommended&#39;,&#39;Not Recommended&#39;]
proportions = [percentage,(100-percentage)]
colors = [&#39;b&#39;, &#39;y&#39;]
plt.pie(proportions, labels=items, colors=colors,startangle=20, shadow=True,
explode=(0.1, 0),radius=1.2, autopct=&#39;%1.1f%%&#39;)
plt.title(&#39;Recommendation System&#39;)
plt.legend()
plt.show()
# Naive Bayes Algorithm
class NaiveBayes:
    def __init__(self):
        self.positive_count = 0



        self.negative_count = 0
        self.positive_words = []
        self.negative_words = []
        self.positive_probability = 0
        self.negative_probability = 0
        self.unique_words = []
        self.unique_count = 0
        self.testing_words = []
        self.positive_testing_probability = []
        self.negative_testing_probability = []
        self.positivity = 0
        self.negativity = 0
        self.positive_posterior = []
        self.negative_posterior = []
        self.resultset = []
        self.accuracy_comapare = []
    def fit(self, sentiment,reviews):
#seperating the positive words and negative words from the reviews.
        for i in range(len(reviews)):
            value = reviews[i].split(&#39; &#39;)
            value.pop(0)
            if (sentiment[i] == &#39;1&#39;):



                self.positivity+=1
                for j in range(len(value)):
                    self.positive_count += 1
                    self.positive_words.append(value[j])
            else:
                self.negativity+=1
                for j in range(len(value)):
                    self.negative_count += 1
                    self.negative_words.append(value[j])
#calculating the postive and negative probaility
        self.positive_probability = self.positivity / self.positivity + self.negativity
        self.negative_probability = self.negativity / self.positivity + self.negativity
#Finding the unique words
  for i in range(len(self.positive_words)):
            if (self.positive_words[i] not in self.unique_words):
                self.unique_words.append(self.positive_words[i])
                self.unique_count+=1
for i in range(len(self.negative_words)):
            if (self.negative_words[i] not in self.unique_words):
                self.unique_words.append(self.negative_words[i])
                self.unique_count+=1
def predict(self,sentiment,reviews):



  for i in range(len(reviews)):
        value = reviews[i].split(&#39; &#39;)
        value.pop(0)
        self.testing_words.append(value)
self.accuracy_comapare = sentiment
# positive
        for i in range(len(self.testing_words)):
  probi = []
            for elem in self.testing_words[i]:
                if (elem in self.positive_words):
                    numerator = self.positive_words.count(elem) + 1
                else:
                    numerator = 1
                prob = numerator / (self.positive_count + self.unique_count)
                probi.append(prob)
            self.positive_testing_probability.append(probi)
      #negative
        for i in range(len(self.testing_words)):
            probi = []
            for elem in self.testing_words[i]:
                if (elem in self.negative_words):
                    numerator = self.negative_words.count(elem) + 1



                else:
                    numerator = 1
                prob = numerator / (self.negative_count + self.unique_count)
                probi.append(prob)
            self.negative_testing_probability.append(probi)
            #positive_posterior value
            lis = []
            for i in range(len(self.positive_testing_probability)):
                value = self.positive_probability
                for elem in self.positive_testing_probability[i]:
                    value = value * elem
                lis.append(value)
            self.positive_posterior = lis
            #negative_posterior value
            lis = []
            for i in range(len(self.negative_testing_probability)):
                value = self.negative_probability
                for elem in self.negative_testing_probability[i]:
                    value = value * elem
                lis.append(value)
            self.negative_posterior = lis
        for i in range(len(self.positive_posterior)):



            if(self.positive_posterior[i] &gt; self.negative_posterior[i]):
                difference = self.positive_posterior[i] - self.negative_posterior[i]
                if(difference &gt; 0.2):
                    self.resultset.append(1.5)
                else:
                    self.resultset.append(1)
            else:
                difference = self.negative_posterior[i] - self.positive_posterior[i]
                if(difference &gt; 0.2):
                    self.resultset.append(-0.5)
                else:              
                    self.resultset.append(0)
        return self.resultset
