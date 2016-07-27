### Intro

##### Material

The introduction to the course. What is machine learning, some applications and how are we going to come at it. What are we going to learn and how are we going to be assessed.

##### Thoughts on the teaching

I liked;
* that you ran the course outline past us, and let us/asked us to give some input. It felt like we have more of a say in what we are going to learn and how. I feel empowered. (dont know if this was by design or disorganisation... but it was good)
* Getting two people to lecture the class tomorrow. Sets a great precedent for; diving into new topics, not feeling pressure to be great, ...?

Improvements(?);
* Could have done with more inspiration. Interesting point you made "_ I dont want to act as a repository for interesting resources, as I want others to go out and find it._" Chicken and egg problem? Need to inspire them first, so they will be motivated to find interesting stuff?
* Get to know class members? Everyone introduces themselves? Why are they taking the course?


*****

### Strawman

##### Material

Two students did the lecturing. A couple of very simple algorithms.
k-NN. So in the learning phase of this algorithm you... save the data into memory, done.

k-means. Iterative.
PCA (did we end up covering this... forgot)

##### Thoughts on the teaching

Was fun. Ideally the students would also have looked at some material on what is being
At one point you took over from one of the lecturing students and he kind of just stood up the front. I think you should have given him the opportunity to try to answer it (whatever the question was). Hopefully, if he does a bad job other students will point it out, or you can come in.

*****

### Perceptrons and the curse

##### Material

A perceptron. Linear threshold. A decision hyperplane -> we know that w.x = 0 if w and x are perpendicular, and is negative if pointing in different directions ... So really we are trying to find the optimal angle between w and the average x (?). How does the loss function $\frac{1}{2}(y - w.x)^2 $ tell us to find this angle?

The curse. $V_i = 2\pi/n V_{i-2}$. A unit circle in a unit square. In 20 dimensions the vast majority of the volume is in the corners of the unit square and almost none is in the circle.
Marcus mentioned that you could figure this out by randomly sampling points and seeing that they will almost always not be in the unit sphere. Is this true? So because it is unlikely it means the volume is small? This link doesnt seem obvious/clear.

##### Thoughts on the teaching

More disorganised than before.
I think the perceptron is a great canidate for people to go away and implement. Shouldnt bother lecturing it.
The curse of dimensionality wasnt linked into ML problems.

*****
### Distributions
##### Material

A look at the softmax function and gaussian distributions. For two class classification the softmax function is a sigmoid. Biases cancel out??? How good an hyperprior is assuming our variables are gaussian? Supposedly if you randomly sample any distribution you get a gaussian??? Covariance matrices are not orthogonal, hmm, but are symmetric and semi-positive definite. Central limit theorem??

##### Thoughts on the teaching

So we have swapped Marcus lecturing for students lecturing, aka worse teachers. I think we/Marcus have missed the point of peer teaching. I think it is peer tutoring that is most beneficial for all, not peer lecturing, which is only really useful for the person lecturing.

*****
### Loss function
##### Material

Covered i.i.d assumption that each point in our data set is independent and is draw from the same distribution. (does this imply that we are assuming that the variables we are sampling are representative of all behaviour?). 

All training can be formulated as the maximisation of the probability that our prediction, given some input, equals the target. P(T=y|x). I feel like there is a way to cheat this?

##### Thoughts on the teaching

Better class. I liked the couple of question we had, some puzzles to solve. The class is starting to get more relaxed and talkative? 

***
### Polynomial curve fitting
##### Material

Didn't understand the problem very well (too cocky..). How can we use polynomial curve fitting for classification? We want to classify different inputs into classes. My answer was to classify different outputs...

##### Thoughts on the class

More coherent and well thought out presentation from the student.
***
### Backprop
##### Material

A detail oriented intro to the chain rule and backprop. I would have liked a higher level explanation, how is it actually propagating anything? Why do we bother?

##### Thoughts on the class

Too many details. We should let people figure that stuff out themselves, go home and try and derive it. As long as they know what the goal is, and what chain rule is, they should be fine.
