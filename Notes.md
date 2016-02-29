# t-SNE
## Local structure vs global structure

Which is really the goal. 
* People like t-SNE because it seperates the classes into categories, but it seems to miss more of the local structure in doing so??? 
  * 1s that look like 4s... 6s that look like 0s? Or does it not?
* 

Coil20 t-SNE looks weird! What is the reason, and how does that picture help us understand the structure of the data?
"The crowding problem"

https://lvdmaaten.github.io/publications/papers/AISTATS_2009.pdf
http://nbviewer.jupyter.org/urls/gist.githubusercontent.com/AlexanderFabisch/1a0c648de22eff4a2a3e/raw/59d5bc5ed8f8bfd9ff1f7faa749d1b095aa97d5a/t-SNE.ipynb

# 311

## Learning math. 
* (Currently) the ideas are obvious, it is about learning the notation. 
 * The lecturers must think we are idiots, they are too focused on their average student passing the dumb it down too much. Thus the average student get bored anyway... Teaching occurs a lot slower.
 * And what are all the kids in my class thinking?!? Do they realise what the point of him droning on about how a = a, or ...
* So the metacognitive technique here would be that I need to figure out what the teacher is trying to teach.
* The issue with many students study technique. Sitting in lectures confused and not following, they should as questions, of the lecturer or google... preferable both

Answering questions and talking to the lecturer. I dont want others to judge me as being the try hard, but what is so bad about that?

* The stereotypes in my class. What is the experience like? Bored students... Blog!
 * The extroverted who does quite know..
 * The super pedantic and perfectionist who doesnt get social ques.
 * 

## Questions

# 313

Learning about the open set. Why?? What is the motivation, the lecturer seem to commonly skip the most important part! Is the just in math courses? Why, because the reason seems obvious to them, because?? I should ask what the motivation is!! That is a good question.
So the open set implies/demands continuious space.

Dont know if I am sold on the definition of 'close' ness (seems like some ad-hoc measure of similarity). e.g. If A is close to b then it is in A... So open sets are arbitrarily large as long as they dont meet some sort of discontinuity? (lecturer - yes)

Definition of a topological space. X where X is a specified collection of open sets. Wouldn't this also work with closed sets? (lecturer - yes)  What is the union of a set of closed sets? 

So a klien bottle is a mobuis strip rotated about 360 degrees, or in a higher dimension. So if you are on the surface of a klein bottle, you can travel in two dimensions. Up, which is the mobious strip, and across, wich is just a cylinder. Can you make it so that both directions result in the mobius strip? How many dimensions would you need to represent this? This could probably be stated (/claculated) mathematically.

The union of a set of open sets it an open set? But this would infer that a surface is open??? Yes. To infinity , or looping back to itself.


# CS231n

* The greater the depth the more the gradients vanish/explode. How do deep conv nets avoid this? Normalise the weights to be on average 1. Thus, between each layer $\delta \cdot w = \delta \cdot 1$. That applies to linear depth, but what about residual nets?
* How does dropout work in conv nets? it is not like we have hidden layers were it is not a big deal if nodes disappear. The means between each layer you need to be able to ?? Dropping a node is the same as removing a column?
* CNNs are attractive because of their efficiency. The weight tying means that less parameters need to be learned. This is why recurrent NNs are also capable of learning interesting things in/with reasonable amount of training data and computational steps.
 * This seems really important. How can it be taken further? 
 * This also seems deeply linked with the use of convolution?
 * 
 
# 335

Why are these lecturers at Vic? A place where there is little interesting research (assumption)...

Real algorithms are too complicated (redundancy...???, finite memory???) so we make a nicer version - Turing machines - full of assumptions and ideals... This does not sound like a good presmise to start on... What is the study of real algorithms and problems? Just timing them and recording the CPU/GPU activity? 

What is the point of non-deterministic turning machines? To model ?? real computers, as electonics makes mistakes, bits accidentally flipped etc...
