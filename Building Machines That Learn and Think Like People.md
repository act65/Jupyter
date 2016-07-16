> In their influential textbook, Russell and Norvig (2003) state that “The quest for ‘artificial flight’ succeeded when the Wright brothers and others stopped imitating birds and started using wind tunnels and learning about aerodynamics.”

So we cautiously draw analogies for how to design thinking machines from human cognition, as it is our best model for intelligence. We think intelligent machines should;

* build models of their environments that seek to explain causes, not just predict features.
* ground learning based in a fundamental understanding of physics (e.g. existence, persistence, ...) and psychology (agency, goals, ...).
* deconstruct their knowledge into smaller discrete representations that can be composed together.
* learn to learn.


You can find the original paper [here](https://arxiv.org/abs/1604.00289).

# Models

> We view learning as a form of model building, or explaining observed data through the construction of causal models of the world.

This is an interesting statement, as at first I am not sure I entirely agree with it. Obviously CNNs, RNNs and DQNs are capable of learning and yet they are (mostly) model-free. 

##### Model building

> Connectionist learning algorithms have been shown to learn powerful models, yet their local and incremental nature seems at odds with important aspects of human learning. Many of the most impressive examples of human learning are better characterised as rapid model building than gradual improvements in pattern recognition.

What is a model? What is the best way to learn a model? To test and experiment? To try to reproduce? What if you have a teacher, how does that help?

**Q:** How would **supervised model learning** work?

Teacher -> student: These are the features you should have used to get to this result, and this is the process you should follow.

##### The combination of two styles of learning

After reading Steven Pinker’s book - The stuff of thought - I have been carrying around his idea that there are two competing processes in the brain.

> words are either stored directly with their associated meanings, in a "mental dictionary", or constructed using morphological rules.

Steven uses the example of irregular verbs, start - started is regular, as it follows a pattern like many other words, end - ended. But, drive - drove is irregular as it doesn’t follow a pattern. My thoughts on this were that there must be some competing process between memory and generalisation for us to learn this sort of thing. And I think the model-free and model-based frame work captures this process. Model-free would/could learn the irregular verbs, while model-based would learn regular verbs.

> ... humans (may) combine model-based and model-free learning algorithms both competitively and cooperatively, and that these interactions are supervised by metacognitive processes.

The interesting thing about the model-free system is that it is fast (generally a feed-forward process). Parallels can be drawn between this and heuristics that people learn (or our intuitions). 

I think this is the benefit of model-free, feed-forward networks. Like the CNNs and DQNs we see in many applications. They are efficient (kinda) and fast (at acting, not learning). So, we seem to have the ability to act fast and learn slow, but can we do it the other way around? Slow acting and fast learning? Or is that a false dichotomy?

**Q:** How can model-free learning help teach a model-based system, a type of **self-teaching**? And vice versa.

I think the steps forward would be to get a fast learner working and then try to integrate the two types together. Maybe we can even use one to teach the other?

> One boundary condition on this flexibility is the fact that the skills become “habitized” with routine application, possibly reflecting a shift from model-based to model-free control

So in relation to the irregular verbs before. Initially we would learn the regular verbs through a model-based process, but then as they become habit, we would learn them through a model-free process. What is nice about this is that: when learning the language initially, the model helps guide us and infer structure.

So, how would this work in a neural net? 

# Foundations

> (Intelligent systems should) ground learning in intuitive theories of physics and psychology, to support and enrich the knowledge that is learned.

One of the biggest puzzles/problems with this line of thought is that we do not know how much humans are preprogrammed with through their genetics. This is important because we don't know how much children learn from their environment. Or in other words, a slightly deeper question, how much is possible to learn from given information.

Pretty much, the more assumptions you can make, the faster you can learn and infer things. But, the more you risk being wrong.

##### Physics

> … incorporating a physics-engine-based representation could help DQNs learn to play games ... faster and (in a) more general way?

Are we sure we want to base thought in physics? Intuitively it makes sense, we live in the physical world, and everything we build is, in some sense, physical. But does this apply to machines living in the digital world? I think it requires more thought. 

I think that for the time being, it is a good goal, but maybe one we should reanalyse after its success.

This raises the idea that we could use a physical-net as a module that higher order NNs can be built ontop of. This leads directly onto the idea of compositionality, which is covered later.

##### Psychology

> A child watching someone play a new video game can infer that the avatar has agency and is trying to seek reward while avoiding punishment. This inference immediately constrains other inferences, allowing the child to infer what objects are good and what objects are bad.

An introductory problem of this would be to learn to predict the goals of different agents in an environment using model-free networks.

Where eventually we would want to learn to build nets that can learn models of the agents and their goals. (is this really necessary? how well can just the model free version do?) 

# Composition

> an infinite number of representations can be constructed from a finite set of primitives.

So, this is about more than having primitive components, it is about having modular representations that can be composed together.

**Q:** What are the best primitive components to use? Can this be formulated in information-theoretic terms? 

> Representing this compositional structure explicitly is both more economical and better for generalisation.

I agree that it would be more efficient, as we have effectively created hashes for specific features. However, I don’t quite get why it would be better for generalisation.

Maybe because we are assuming that everything is made from the same components, thus we have less search space?

Can we already do this? For example lets consider a CNN. In the first convolutional layer it learns a set of features, we could consider these the primitive features. It then composes these together to form more complex features, which themselves can be composed to form more complex features, and so on... How is this different? 

In practice, this concept seems deeply tied to invariance and weight tying.

# Learning to learn

> (How can) ... learning a new task can be accelerated through previous or parallel learning of other related tasks.

I like their inclusion of parallel learning here. I had not considered that, but it makes a lot of sense. I see active learning as a stepping stone into this type of problem.

> The ‘child as scientist’ proposal further views the process of learning itself as also scientist-like, with recent experiments showing that children seek out new data to distinguish between hypotheses, isolate variables, test causal hypotheses, make use of the data-generating process in drawing conclusions, and learn selectively from others.


Not much to say about this, I love these two ideas (learning to learn and active learning). Now I just need to make it work. 

> People transfer knowledge at multiple levels, from low-level perception to high-level strategy, exploiting compositionality at all levels.

Because all knowledge is built on some shared components the knowledge can be transferred. So it is almost like a type of knowledge invariance??? Where we have some sort of basic knowledge that applies to every/all applications. I guess this comes back to the physical and psychological foundations. 

> Since the parts and relations are themselves a product of previous learning, their facilitation of the construction of new models is also an example of learning-to-learn

To be clear, they are really talking about a process for learning faster, not learning how to learn faster. Since we have already learnt the primitive components of our environment, we don’t need to relearn them every time we see something new.

# Challenges

* Learning (or making inferences) from small amounts of sparse data
* Learning goal invariance
* Learning models
* Build an AI system that beats a world-class player with the amount and kind of training human champions receive – rather than overpowering them with Google-scale computational resources.

# Other stuff

##### Goal invariance. 

How the hell do you learn that?

>For example, imagine playing Frostbite with one of these goals:
Get the lowest possible score. Get closest to 100, or 300, or 1000, or 3000, or any level, without going over. Beat your friend, who’s playing next to you, but just barely, not by too much, so as not to embarrass them. Teach your friend how to play as efficiently as possible.
This range of goals highlights an essential component of human intelligence: people can learn models and use them for arbitrary new goals and tasks with little or no retraining or reconfiguration.

However, these changes in goals would be disastrous for any of our current learning algorithms.


##### Exhaustive search

Who said learning was efficient?

Sometimes the only solution is to do uninformed search. I mean how quickly have humans solved some complex problems, quantum physics, ... machine learning... Or how long does it take humans to learn complex ideas like math?

> Even without knowing the answer to the question “Where is the deepest point in the Pacific Ocean?” one still knows that the answer must be a location on a map. (Alternatively), the answer “20 inches” to the question “What year was Lincoln born?” can be invalidated a priori, even without knowing the correct answer.

So would this frame inference as the process of maximally reducing search space? Or somehow structuring our search space?

