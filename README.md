<!-- This is the markdown template for the final project of the Building AI course, 
created by Reaktor Innovations and University of Helsinki. 
Copy the template, paste it to your GitHub README and edit! -->

# Project Title
German AI Assistant

Building AI course project

## Summary

Describe briefly in 2-3 sentences what your project is about. About 250 characters is a nice length! 

I plan to create an AI assistant that will help people interested in learning German by personalizing study sessions for them. It will be able to teach a few new words everyday, quiz a user on previously learned words to ensure memory, and also converse with the user in German to help practice conversational skills. 

## Background

Which problems does your idea solve? How common or frequent is this problem? What is your personal motivation? Why is this topic important or interesting?

This is how you make a list, if you need one:
* problem 1
* problem 2
* etc.

This AI assistant will solve a few problems:
* Helping a user to memorize grammar rules
* Helping a user to memorize the gender of nouns (der, die, das)
* Teaching words in context
* Creating a personalized approach to studying that will prevent burnout and loss of motivation

These problems are frequent when learning German as it has a lot of complicted rules regarding grammar, sentence structure and gender of nouns. My personal motivation stems from me learning German the past few months and encountering these issues myself. This topic is important because German is quite a popular language and for those who want to learn it, especially for those emigrating to a German-speaking country, my project will be able to help them greatly.


## How is it used?

Describe the process of using the solution. In what kind situations is the solution needed (environment, time, etc.)? Who are the users, what kinds of needs should be taken into account?

My project would be used by anyone interested in learning German, whenever they want. If they want to review any words they learned, they can ask it to generate a short quiz. If they want to practice a quick conversation, they will be able to do that. Some needs to be taken into account is the numerous studying strategies available — if this AI assistant is to be personalized, it should be able to offer different studying ideas for users.

Images will make your README look nice!
Once you upload an image to your repository, you can link link to it like this (replace the URL with file path, if you've uploaded an image to Github.)
![Cat](https://upload.wikimedia.org/wikipedia/commons/5/5e/Sleeping_cat_on_her_back.jpg)

If you need to resize images, you have to use an HTML tag, like this:
<img src="https://upload.wikimedia.org/wikipedia/commons/5/5e/Sleeping_cat_on_her_back.jpg" width="300">

This is how you create code examples:
```
def main():
   countries = ['Denmark', 'Finland', 'Iceland', 'Norway', 'Sweden']
   pop = [5615000, 5439000, 324000, 5080000, 9609000]   # not actually needed in this exercise...
   fishers = [1891, 2652, 3800, 11611, 1757]

   totPop = sum(pop)
   totFish = sum(fishers)

   # write your solution here

   for i in range(len(countries)):
      print("%s %.2f%%" % (countries[i], 100.0))    # current just prints 100%

main()
```

## Data sources and AI methods
Where does your data come from? Do you collect it yourself or do you use data collected by someone else?
If you need to use links, here's an example:
[Twitter API](https://developer.twitter.com/en/docs)

| Syntax      | Description |
| ----------- | ----------- |
| Header      | Title       |
| Paragraph   | Text        |

I will use data from the official German language, so lists of nouns, verbs, their past tenses, etc. That way my model will have a vast knowledge base of the German language and its rules.

## Challenges

What does your project _not_ solve? Which limitations and ethical considerations should be taken into account when deploying a solution like this?

Because I am not so familiar with creating AI projects, my first iteration may have chances of making mistakes such as misspelling words, using wrong grammar rules, etc. I would advise this project to be used alongside regular human learning, either through self-studying or by a teacher. As for ethical considerations, something that should be taken into account is what data is used to personalize the studying. It should not infringe on user privacy concerns. 

## What next?

How could your project grow and become something even more? What kind of skills, what kind of assistance would you  need to move on? 

My project could potentially grow into it's own website like ChatGPT, adding even more features to help users grasp the German language. I would need assistance from official German-teaching institutes and maybe even the German, Austrian, Swiss, Luxembourgish, etc. governments to offer information that could make my project more accessible and professional.

## Acknowledgments

* list here the sources of inspiration

My sources of inspiration are primarily me learning the German language personally and encountering many of these issues myself, like struggling with the sentence structure and gendered nouns.

* do not use code, images, data etc. from others without permission
* when you have permission to use other people's materials, always mention the original creator and the open source / Creative Commons licence they've used
  <br>For example: [Sleeping Cat on Her Back by Umberto Salvagnin](https://commons.wikimedia.org/wiki/File:Sleeping_cat_on_her_back.jpg#filelinks) / [CC BY 2.0](https://creativecommons.org/licenses/by/2.0)
* etc
