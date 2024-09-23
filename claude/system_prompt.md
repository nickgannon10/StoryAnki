How to write good prompts: using spaced repetition to create understanding
Andy MatuschakTwitter logo

December 2020

contents

The central role of retrieval practice
Properties of effective retrieval practice prompts
A recipe for chicken stock
Factual knowledge
Simple facts
Lists
Cues and elaborative encoding
Interpretation; the “more than you think” rule of thumb
Procedural knowledge
Conceptual knowledge
Open lists
Salience prompts
Prompt-writing, in practice
Iterative prompt-writing
Litmus tests
Revising prompts over time
This guide and its embedded spaced repetition system were made possible by a crowd-funded research grant from my Patreon community. If you find my work interesting, you can become a member to get ongoing behind-the-scenes updates and early access to new work.

Special thanks to my sponsor-level patrons: Adam Wiggins, Andrew Sutherland, Bert Muthalaly, Calvin French-Owen, Dwight Crow, fnnch, James Hill-Khurana, Lambda AI Hardware, Ludwig Petersson, Mickey McManus, Mintter, Patrick Collison, Paul Sutter, Peter Hartree, Sana Labs, Shripriya Mahesh, Tim O’Reilly.

As a child, I had a goofy recurring daydream: maybe if I type just the right sequence of keys, the computer would beep a few times in sly recognition, then a hidden world would suddenly unlock before my eyes. I’d find myself with new powers which I could use to transcend my humdrum life.

Such fantasies probably came from playing too many video games. But the feelings I have when using spaced repetition systems are strikingly similar. At their best, these systems feel like magic.This guide assumes basic familiarity with spaced repetition systems. For an introduction, see Michael Nielsen, Augmenting Long-term Memory (2018), which is also the source of the phrase “makes memory a choice.” Memory ceases to be a haphazard phenomenon, something you hope happens: spaced repetition systems make memory a choice. Used well, they can accelerate learning, facilitate creative work, and more. But like in my childhood daydreams, these wonders unfold only when you press just the right sequence of keys, producing just the right incantation. That is, when you manage to write good prompts—the questions and answers you review during practice sessions.

Spaced repetition systems work only as well as the prompts you give them. And especially when new to these systems, you’re likely to give them mostly bad prompts. It often won’t even be clear which prompts are bad and why, much less how to improve them. My early experiments with spaced repetition systems felt much like my childhood daydreams: prodding a dusty old artifact, hoping it’ll suddenly spring to life and reveal its magic.

Happily, prompt-writing does not require arcane secrets. It’s possible to understand somewhat systematically what makes a given prompt effective or ineffective. From that basis, you can understand how to write good prompts. Now, there are many ways to use spaced repetition systems, and so there are many ways to write good prompts. This guide aims to help you create understanding in the context of an informational resource like an article or talk. By that I mean writing prompts not only to durably internalize the overt knowledge presented by the author, but also to produce and reinforce understandings of your own, understandings which you can carry into your life and creative work.

For readers who are new to spaced repetition, this guide will help you overcome common problems that often lead people to abandon these systems. In later sections, we’ll cover some unusual prompt-writing perspectives which may help more experienced readers deepen their practice.If you don’t have a spaced repetition system, I’d suggest downloading Anki and reading Michael’s aforementioned essay. Our discussion will focus on high-level principles, so you can follow along using any spaced repetition system you like. Let’s get started.

The central role of retrieval practice
No matter the application, it’s helpful to remember that when you write a prompt in a spaced repetition system, you are giving your future self a recurring task. Prompt design is task design.

If a prompt “works,” it’s because performing that task changes you in some useful way. It’s worth trying to understand the mechanisms behind those changes, so you can design tasks which produce the kind of change you want.

The most common mechanism of change for spaced repetition learning tasks is called retrieval practice. In brief: when you attempt to recall some knowledge from memory, the act of retrieval tends to reinforce those memories.For more background, see Roediger and Karpicke, The Power of Testing Memory (2006). Gwern Branwen’s article on spaced repetition is a good popular overview. You’ll forget that knowledge more slowly. With a few retrievals strategically spaced over time, you can effectively halt forgetting. The physical mechanisms are not yet understood, but hundreds of cognitive scientists have explored this effect experimentally, reproducing the central findings across various subjects, knowledge types (factual, conceptual, procedural, motor), and testing modalities (multiple choice, short answer, oral examination).

The value of fluent recall isn’t just in memorizing facts. Many of these experiments tested students not with parroted memory questions but by asking them to make inferences, draw concept mapsSee e.g. Karpicke and Blunt, Retrieval Practice Produces More Learning than Elaborative Studying with Concept Mapping (2011); and Blunt and Karpicke, Learning With Retrieval-Based Concept Mapping (2014)., or answer open-ended questions. In these studies, improved recall translated into improved general understanding and problem-solving ability.

Retrieval is the key element which distinguishes this effective mode of practice from typical study habits. Simply reminding yourself of material (for instance by re-reading it) yields much weaker memory and problem-solving performance. The learning produced by retrieval is called the “testing effect” because it occurs when you explicitly test yourself, reaching within to recall some knowledge from the tangle of your mind. Such tests look like typical school exams, but in some sense they’re the opposite: retrieval practice is about testing your knowledge to produce learning, rather than to assess learning.

Spaced repetition systems are designed to facilitate this effect. If you want prompts to reinforce your understanding of some topic, you must learn to write prompts which collectively invoke retrieval practice of all the key details.

We’ll have to step outside the scientific literature to understand how to write good prompts: existing evidence stops well short of exact guidance. In lieu of that, I’ve distilled the advice in this guide from my personal experience writing thousands of prompts, grounded where possible in experimental evidence.

For more background on the mnemonic medium, see Matuschak and Nielsen, How can we develop transformative tools for thought? (2019).This guide is an example of what Michael Nielsen and I have called a mnemonic medium. It exemplifies its own advice through spaced repetition prompts interleaved directly into the text. If you’re reading this, you’ve probably already used a spaced repetition system. This guide’s system, Orbit, works similarly.If you have an existing spaced repetition practice, you may find it annoying to review prompts in two places. As Orbit matures, we’ll release import / export tools to solve this problem. But it has a deeper aspiration: by integrating expert-authored prompts into the reading experience, authors can write texts which readers can deeply internalize with relatively little effort. If you’re an author, then, this guide may help you learn how to write good prompts both for your personal practice and also for publications you write using Orbit. You can of course read this guide without answering the embedded prompts, but I hope you’ll give it a try.


These embedded prompts are part of an ongoing research project. The first experiment in the mnemonic medium was Quantum Country, a primer on quantum computation. Quantum Country is concrete and technical: definitions, notation, laws. By contrast, this guide mostly presents heuristics, mental models, and advice. The embedded prompts therefore play quite different roles in these two contexts. You may not need to memorize precise definitions here, but I believe the prompts will help you internalize the guide’s ideas and put them into action. On the other hand, this guide’s material may be too contingent and too personal to benefit from author-provided prompts. It’s an experiment, and I invite you to tell me about your experiences.

One important limitation is worth noting. This guide describes how to write prompts which produce and reinforce understandings of your own, going beyond what the author explicitly provides. Orbit doesn’t yet offer readers the ability to remix author-provided prompts or add their own. Future work will expand the system in that direction.

Properties of effective retrieval practice prompts
Writing good prompts feels surprisingly similar to translating written text. When translating prose into another language, you’re asking: which words, when read, would light a similar set of bulbs in readers’ minds? It’s not a rote operation. If the passage involves allusion, metaphor, or humor, you won’t translate literally. You’ll try to find words which recreate the experience of reading the original for a member of a foreign culture.

When writing spaced repetition prompts meant to invoke retrieval practice, you’re doing something similar to language translation. You’re asking: which tasks, when performed in aggregate, require lighting the bulbs which are activated when you have that idea “fully loaded” into your mind?

The retrieval practice mechanism implies some core properties of effective prompts. We’ll review them briefly here, and the rest of this guide will illustrate them through many examples.

These properties aren’t laws of nature. They’re more like rules you might learn in an English class. Good writers can (and should!) strategically break the rules of grammar to produce interesting effects. But you need to have enough experience to understand why doing something different makes sense in a given context.

Retrieval practice prompts should be focused. A question or answer involving too much detail will dull your concentration and stimulate incomplete retrievals, leaving some bulbs unlit. Unfocused questions also make it harder to check whether you remembered all parts of the answer and to note places where you differed. It’s usually best to focus on one detail at a time.

Retrieval practice prompts should be precise about what they’re asking for. Vague questions will elicit vague answers, which won’t reliably light the bulbs you’re targeting.

Retrieval practice prompts should produce consistent answers, lighting the same bulbs each time you perform the task. Otherwise, you may run afoul of an interference phenomenon called “retrieval-induced forgetting”This effect has been produced in many experiments but is not yet well understood. For an overview, see Murayama et al, Forgetting as a consequence of retrieval: a meta-analytic review of retrieval-induced forgetting (2014).: what you remember during practice is reinforced, but other related knowledge which you didn’t recall is actually inhibited. Now, there is a useful type of prompt which involves generating new answers with each repetition, but such prompts leverage a different theory of change. We’ll discuss them briefly later in this guide.

SuperMemo’s algorithms (also used by most other major systems) are tuned for 90% accuracy. Each review would likely have a larger impact on your memory if you targeted much lower accuracy numbers—see e.g. Carpenter et al, Using Spacing to Enhance Diverse Forms of Learning (2012). Higher accuracy targets trade efficiency for reliability.Retrieval practice prompts should be tractable. To avoid interference-driven churn and recurring annoyance in your review sessions, you should strive to write prompts which you can almost always answer correctly. This often means breaking the task down, or adding cues.

Retrieval practice prompts should be effortful. It’s important that the prompt actually involves retrieving the answer from memory. You shouldn’t be able to trivially infer the answer. Cues are helpful, as we’ll discuss later—just don’t “give the answer away.” In fact, effort appears to be an important factor in the effects of retrieval practice.For more on the notion that difficult retrievals have a greater impact than easier retrievals, see the discussion in Bjork and Bjork, A New Theory of Disuse and an Old Theory of Stimulus Fluctuation (1992). Pyc and Rawson, Testing the retrieval effort hypothesis: Does greater difficulty correctly recalling information lead to higher levels of memory? (2009) offers some focused experimental tests of this theory, which they coin the “retrieval effort hypothesis.” That’s one motivation for spacing reviews out over time: if it’s too easy to recall the answer, retrieval practice has little effect.

Achieving these properties is mostly about writing tightly-scoped questions. When a prompt’s scope is too broad, you’ll usually have problems: retrieval will often lack a focused target; you may produce imprecise or inconsistent answers; you may find the prompt intractable. But writing tightly-scoped questions is surprisingly difficult. You’ll need to break knowledge down into its discrete components so that you can build those pieces back up as prompts for retrieval practice. This decomposition also makes review more efficient. The schedule will rapidly remove easy material from regular practice while ensuring you frequently review the components you find most difficult.

Now imagine you’ve just read a long passage on a new topic. What, specifically, would have to be true for you to say you “know” it? To continue the translation metaphor, you must learn to “read” the language of knowledge—recognizing nouns and verbs, sentence structures, narrative arcs—so that you can write their analogues in the translated language. Some details are essential; some are trivial. And you can’t stop with what’s on the page: a good translator will notice allusions and draw connections of their own.

So we must learn two skills to write effective retrieval practice prompts: how to characterize exactly what knowledge we’ll reinforce, and how to ask questions which reinforce that knowledge.


A recipe for chicken stock
Our discussion so far has been awfully abstract. We’ll continue by analyzing a concrete example: a recipe for chicken stock.

A recipe may seem like a fairly trivial target for prompt-writing, and in some sense that’s true. It’s a conveniently short and self-contained example. But in fact, my spaced repetition library contains hundreds of prompts capturing foundational recipes, techniques, and observations from the kitchen. This is itself an essential prompt-writing skill to build—noticing unusual but meaningful applications for prompts—so I’ll briefly describe my experience.

I’d cooked fairly seriously for about a decade before I began to use spaced repetition, and of course I naturally internalized many core techniques and ratios. Yet whenever I was making anything complex, I’d constantly pause to consult references, which made it difficult to move with creativity and ease. I rarely felt “flow” while cooking. My experiences felt surprisingly similar to my first few years learning to program, in which I encountered exactly the same problems. With years of full-time attention, I automatically internalized all the core knowledge I needed day-to-day as a programmer. I’m sure that I’d eventually do the same in the kitchen, but since cooking has only my part-time attention, the process might take a few more decades.

I started writing prompts about core cooking knowledge three years ago, and it’s qualitatively changed my life in the kitchen. These prompts have accelerated my development of a deeply satisfying ability: to show up at the market, choose what looks great in that moment, and improvise a complex meal with confidence. If the sunchokes look good, I know they’d pair beautifully with the mustard greens I see nearby, and I know what else I need to buy to prepare those vegetables as I imagine. When I get home, I already know how to execute the meal; I can move easily about the kitchen, not hesitating to look something up every few minutes. Despite what this guide’s lengthy discussion might suggest, these prompts don’t take me much time to write. Every week or two I’ll trip on something interesting and spend a few minutes writing prompts about it. That’s been enough to produce a huge impact.

At a decent restaurant, even simple foods often taste much better than most home cooks’ renditions. Sautéed vegetables seem richer; grains seem richer; sauces seem more luscious. One key reason for this is stock, a flavorful liquid building block. Restaurants often use stocks in situations where home cooks might use water: adding a bit of steam to sautéed vegetables, thinning a purée, simmering whole grains, etc. Stocks are also the base of many sauces, soups, and braises.

Stock is made by simmering flavorful ingredients in water. By varying the ingredients, we can produce different types of stock: chicken stock, vegetable stock, mushroom stock, pork stock, and so on. But unlike a typical broth, stock isn’t meant to have a distinctive flavor that can stand on its own. Instead, its job is to provide a versatile foundation for other preparations.

One of the most useful stocks is chicken stock. When used to prepare vegetables, chicken stock doesn’t make them taste like chicken: it makes them taste more savory and complete. It also adds a luxurious texture because it’s rich in gelatin from the chicken bones. Chicken stock takes only a few minutes of active time to make, and in a typical kitchen, it’s basically free: the primary ingredient is chicken bones, which you can naturally accumulate in your freezer if you cook chicken regularly.

Recipe
2lbs (~1kg) chicken bones
2qt (~2L) water
1 onion, roughly chopped
2 carrots, roughly chopped
2 ribs of celery, roughly chopped
4 cloves garlic, smashed
half a bunch of fresh parsley
Combine all the ingredients in a large pot.
Bring to a simmer on low heat (this will take about an hour). We use low heat to produce a bright, clean flavor: at higher temperatures, the stock will both taste and look duller.
Lower heat to maintain a bare simmer for an hour and a half.
Strain, wait until cool, then transfer to storage containers.
Chicken stock will keep for a week in the fridge or indefinitely in the freezer. There will be a cap of fat on the stock; skim that off before using the stock, and deploy the fat in place of oil or butter in any savory cooking situation.

This recipe can be scaled up or down to the quantity of chicken bones you have. The basic ratio is a pound of bones to a quart of water. The vegetables are flexible in choice and ratio.

Variations
For a more French flavor profile, replace the celery with leeks and add any/all of bay leaves, black peppercorns, and thyme. For a deeper flavor, roast the bones and vegetables first to make what’s called a “brown chicken stock” (the recipe above is for a “white chicken stock,” which is more delicate but also more versatile).

What to do with chicken stock
A few ideas for what you might do with your chicken stock:

Cook barley, farro, couscous and other grains in it.
Purée with roasted vegetables to make soup.
Wilt hearty greens like kale, chard, or collards in oil, then add a bit of stock and cover to steam through.
After roasting or pan-searing meat, deglaze the pan with stock to make a quick sauce.
To organize our efforts, it’s helpful to ask: what would it mean to “know” this material? I’d suggest that someone who “knows” this material should:

know how to make and store chicken stock
know what stock is and (at least shallowly) understand why and when it matters
know the role and significance of chicken stock, specifically
know some ways one might use chicken stock, both generally and with some specific examples
know of a few common variations and when they might be used
Some of this knowledge is factual; some of it is procedural; some of it is conceptual. We’ll see strategies for dealing with each of these types of knowledge.

But understanding is inherently personal. Really “knowing” something often involves going beyond what’s on the page to connect it to your life, other ideas you’re exploring, and other activities you find meaningful. We’ll also look at how to write questions of that kind.

If you’re a vegetarian, I hope you can look past the discussion of bones: choosing this example involved many trade-offs.In this guide, we’ll imagine that you’re an interested home cook who’s never made stock before. Naturally, if you’re an experienced cook, you’d probably need only a few of these prompts. And of course, if you don’t cook at all, you’d write none of these prompts! Try to read the examples as demonstrations of how you might internalize a resource deeply without much prior fluency.

To demonstrate a wide array of principles, we’ll treat this material quite exhaustively. But it’s worth noting that in practice, you usually won’t study resources as systematically as this. You’ll jump around, focusing only on the parts which seem most valuable. You may return to a resource on a few occasions, writing more prompts as you understand what’s most relevant. That’s good! Exhaustiveness may seem righteous in a shallow sense, but an obsession with completionism will drain your gumption and waste attention which could be better spent elsewhere. We’ll return to this issue in greater depth later.

How to make and store chicken stock: factual and procedural knowledge
Chicken stock
At a decent restaurant, even simple foods often taste much better than most home cooks’ renditions. Sautéed vegetables seem richer; grains seem richer; sauces seem more luscious. One key reason for this is stock, a flavorful liquid building block. Restaurants often use stocks in situations where home cooks might use water: adding a bit of steam to sautéed vegetables, thinning a purée, simmering whole grains, etc. Stocks are also the base of many sauces, soups, and braises.

Stock is made by simmering flavorful ingredients in water. By varying the ingredients, we can produce different types of stock: chicken stock, vegetable stock, mushroom stock, pork stock, and so on. But unlike a typical broth, stock isn’t meant to have a distinctive flavor that can stand on its own. Instead, its job is to provide a versatile foundation for other preparations.

One of the most useful stocks is chicken stock. When used to prepare vegetables, chicken stock doesn’t make them taste like chicken: it makes them taste more savory and complete. It also adds a luxurious texture because it’s rich in gelatin from the chicken bones. Chicken stock takes only a few minutes of active time to make, and in a typical kitchen, it’s basically free: the primary ingredient is chicken bones, which you can naturally accumulate in your freezer if you cook chicken regularly.

Recipe
2lbs (~1kg) chicken bones
2qt (~2L) water
1 onion, roughly chopped
2 carrots, roughly chopped
2 ribs of celery, roughly chopped
4 cloves garlic, smashed
half a bunch of fresh parsley
Combine all the ingredients in a large pot.
Bring to a simmer on low heat (this will take about an hour). We use low heat to produce a bright, clean flavor: at higher temperatures, the stock will both taste and look duller.
Lower heat to maintain a bare simmer for an hour and a half.
Strain, wait until cool, then transfer to storage containers.
Chicken stock will keep for a week in the fridge or indefinitely in the freezer. There will be a cap of fat on the stock; skim that off before using the stock, and deploy the fat in place of oil or butter in any savory cooking situation.

This recipe can be scaled up or down to the quantity of chicken bones you have. The basic ratio is a pound of bones to a quart of water. The vegetables are flexible in choice and ratio.

Variations
For a more French flavor profile, replace the celery with leeks and add any/all of bay leaves, black peppercorns, and thyme. For a deeper flavor, roast the bones and vegetables first to make what’s called a “brown chicken stock” (the recipe above is for a “white chicken stock,” which is more delicate but also more versatile).

What to do with chicken stock
A few ideas for what you might do with your chicken stock:

Cook barley, farro, couscous and other grains in it.
Purée with roasted vegetables to make soup.
Wilt hearty greens like kale, chard, or collards in oil, then add a bit of stock and cover to steam through.
After roasting or pan-searing meat, deglaze the pan with stock to make a quick sauce.
We’ll begin with the “recipe” section of this passage, which describes how to make and store chicken stock. It’s interesting to contrast this section’s text with the more conceptual initial paragraphs. As a form, recipes already involve a somewhat more explicit knowledge structure than you’d find in ordinary prose. This will give us a bit of a scaffold to get started.

To know how to make chicken stock, you must know what ingredients to collect. We’ll begin there.

This type of knowledge is mostly factual. There aren’t a lot of concepts or relationships here: it’s mostly just a bunch of raw information you need to know.

Simple facts
We could write a prompt which simply asks: “What do you need to make chicken stock?” But this isn’t precise enough: should we recall the quantities or just the names of the ingredients? How much chicken stock are we making? This isn’t focused enough: because it’s asking for so many details simultaneously, it’s unlikely to sharply activate all the memories you want to reinforce. And because it’s asking for so much, it’s liable to lead to inconsistency and intractability: each time you answer, you’ll remember some details and forget others. The inconsistent activations will tend to erode your memory.

We’ll need to break the ingredients list down into the elements which must actually be learned.

The first line is about the chicken component. If you’d never heard of stock before, you could begin by simply clarifying what kind of chicken we use:

Q. What type of chicken parts are used in stock?

A. Bones.

This question focuses on just one detail. It’s precise about what it wants (“What type of chicken parts…?”), and it should produce a consistent answer over time. It’s plenty tractable, but it still demands the effort of retrieving the answer from memory.

Writing a simple factual prompt like that naturally tickles a neighbor you might consider adding: the explanation prompt. I write prompts like this when a detail seems likely to be challenging or when the explanation itself is interesting. A more experienced cook likely wouldn’t bother with the first question, but they might still find this one useful.

Q. Why do we use bones to make chicken stock?

A. They’re full of gelatin, which produces a rich texture.

The explanation question will reinforce the knowledge captured by the factual question. Perhaps more importantly, explanations make facts more meaningful. A prompt like this offers a hook to connect the fact to other ideas you may pick up in later cooking adventures. For instance, a Chinese dish of jellied chicken feet might inspire you to try using feet as some of the bones in your stock (as in fact, they’re the most gelatin-rich part).

Note that the answer is found in a different section of the text! Writing prompts often involves hopping around as you work to identify the puzzle pieces and put them together.

Now, this explanation prompt is a good first try, but it could be more precise. It would be reasonable to answer “Why do we use bones to make chicken stock?” with “Because bones are economical.” You want to write questions which cause you to unambiguously retrieve the information you have in mind. This more precise prompt is better:

Q. How do bones produce a chicken stock’s rich texture?

A. They’re full of gelatin.


You may notice that one of the prompts in this review set doesn’t satisfy the consistency property. That prompt isn’t trying to engage retrieval practice, at least not like we’ve seen so far. Perhaps it doesn’t work very well—such prompts are a bit of an experiment! We’ll discuss them more later.

Lists
Back to the ingredients list. Chicken stock obviously involves chicken and water: that follows from the definition of stock (which we’ll handle later). But then there are all the aromatic flavorings, which are more variable and depend somewhat on application. Understanding the ingredients in terms of functional grouping will help us internalize the structure of the recipe:

Q. Chicken stock is made with chicken, water, and what other category of ingredients?

A. Aromatics.

From here, we might ask:

Q. What are typical aromatics used in chicken stock?

A. onion, carrots, celery, garlic, and parsley

But unless you’re an experienced cook, you’ll probably find this prompt intractable, or you may remember ingredients inconsistently. Unordered lists like this can be challenging to translate into good prompts.

One good strategy is to create a set of questions which require you to fill in a missing element of the list:

Q. Typical chicken stock aromatics:

???
carrots
celery
garlic
parsley
A. Onion

Q. Typical chicken stock aromatics:

onion
???
celery
garlic
parsley
A. Carrots

… and so on. Note that I keep the list in the same order. When each element has a consistent (though arbitrary) location, you’ll end up learning the list’s visual “shape” to some extent as you repeat these prompts. That will help your recall.

Most spaced repetition software has a special function which can rapidly generate sets of fill-in-the-blank prompts like this. In the software interfaces, these prompts are often called “cloze deletions.” In each review session, the software will only ask you to fill in one blank. This behavior is important because without it, one variant would “give away” the answer to another.

Ultimately, of course, you want to be able to recall all the ingredients on demand, not just one. Much of the time, these single-element deletions will be enough to achieve that goal. But with complex ideas, you may find you need to add integrative prompts after you’ve thoroughly practiced their discrete components. In the case of lists, you can imagine that the system could ask you to fill in more blanks simultaneously as your memory of the individual entries improves. I don’t know of any general memory system which does that, but it seems worth trying. This is one example of a general opportunity to incorporate more sophisticated knowledge modeling into these systems.

Another way to help yourself understand lists like this is to write explanation prompts for each of the components: A quick answer: carrot provides vegetal sweetness; like salt, this sugar brightens other flavors.why is carrot a good aromatic for chicken stock? If you know the answer to this question for each ingredient, you’ll have an easier time generating the list on demand, perhaps without any of the cloze deletions. And as with simple facts, explanations make knowledge more meaningful. In this case, the recipe doesn’t say, so you’d need to do some research to write questions of this kind.


Cues and elaborative encoding
If you find yourself struggling with these prompts, it can be helpful to add a cue, like this:

Q. Typical chicken stock aromatics:

onion
carrots
celery
garlic
??? (herb)
A. Parsley

But make sure the cue doesn’t render the prompt trivial: it’s important that you exert some effort to retrieve the answer from memory. Consider this prompt:

Q. Typical chicken stock aromatics:

onion
??? (rhymes with parrots)
celery
garlic
parsley
A. Carrots

This prompt doesn’t require you to retrieve any knowledge about chicken stock: there’s only one vegetable which rhymes with “parrots.” You could answer this without having ever read the recipe. By contrast, the previous prompt’s cue—“herb”—leaves your memory with work to do. There are many herbs, and you’ll still need to remember which one the recipe specified.

That said, “rhymes with parrots” may be a useful mnemonic device to add to the answer, offering an association to help you in the future:

Q. Typical chicken stock aromatics:

onion
???
celery
garlic
parsley
A. carrots (rhymes with “parrots”: picture a flock of parrots flying with carrots in their mouths, dropping them into a pot of stock)

Such cues engage another memory phenomenon cognitive scientists have explored experimentally: you make information easier to recall when you connect it to other memories. This process is called elaborative encodingSee e.g. Bradshaw and Anderson, Elaborative Encoding as an Explanation of Levels of Processing (1982).. The members of an ingredient list can be difficult to relate to anything meaningful. In such cases, you can still leverage elaborative encoding by fabricating an association as a mnemonic device. Vivid associations work best, so it’s helpful to find relationships involving visuals, meaningful personal experiences, or emotions like humor and disgust.

Putting these mnemonic devices in the answer field is a useful general trick when the information you’re trying to remember seems relatively arbitrary or isolated. By putting the association in parentheses, you’re making it clear that the focus of the prompt is on remembering the answer: the association is an extra tidbit you might engage with, or not.

This particular prompt is unlikely to require any extra help, but if you really find yourself struggling, you can add a prompt specifically intended to reinforce the association:

Q. Mnemonic device for carrots in chicken stock?

A. rhymes with “parrots”: picture a flock of parrots flying with carrots in their mouths, dropping them into a pot of stock

Instead of fabricating a mnemonic device, you can also leverage elaborative encoding by adding imagery to your prompts. The same fill-in-the-blank idea applies quite well to images. You’d probably find this prompt much easier to remember over time than its textual equivalent:

Q. Chicken stock ingredients:


A. Carrots


Of course, cues and elaborative encoding add extra effort. You don’t need to use them all the time: you’d probably find that exhausting. But they’re useful techniques to deploy if you suspect a prompt will prove difficult to remember, or if you’ve noticed yourself struggling in practice.


Interpretation; the “more than you think” rule of thumb
Now we’ve covered the ingredients which go into the stock. What about quantities?

Well, you could try something like: “How much chicken bone is in a batch of chicken stock?” But what’s a “batch”? This question isn’t precise enough. We could appeal to the particular recipe, asking “How much chicken bone is in Andy’s recipe for chicken stock?” But that’s not actually what we want to know: the recipe notes that you’ll want to adjust the recipe for the quantity of chicken bones you’re using. Writing good prompts often involves interpretation, a first step to creating understanding beyond what’s explicitly written.

Q. What’s the ratio of chicken bones to water in chicken stock?

A. A quart of water per pound of bones

Q. How much onion to use in chicken stock per pound of chicken bones?

A. Half an onion per pound

Q. How much carrots/celery to use in chicken stock per pound of chicken bones?

A. 1 carrot/celery rib per pound

Q. How much garlic to use in chicken stock per pound of chicken bones?

A. 2 smashed cloves per pound

What about the parsley? Here’s another instance of interpretation: “a bunch” of parsley is not a consistent unit anyway. So I won’t bother writing prompts about parsley’s quantity; I’ll just grab a handful.

Notice how I’ve broken the ingredient list down into many questions here, each focused and precise. I’ve noticed that people often feel a compulsion to economize on the number of prompts they write. Prompts seem to carry a per-unit “price,” so people naturally try to write fewer questions which cover more ground. But that’s counter-productive. Unless you explicitly decide to exclude certain information, the number of “units of raw knowledge” is fixed, a constant of the territory. When you write coarser prompts in smaller quantity, you’re not reducing the amount you have to learn. You’re just making the material harder to review.

Prompts are cheaper than you probably imagine. An easy prompt will consume 10–30 seconds across the entire first year of practice, and much less in each subsequent year. Until you’ve internalized that observation, try to adopt this rule of thumb: write more prompts than feels natural.

Now, prompts are cheap, but they’re not free. Besides their time cost, they have an emotional cost: no one wants to spend time reviewing a bunch of boring material they already know. So if you’re writing prompts for a subject that’s already quite familiar, you should use fewer prompts—not because it’s always safe to write coarser questions for familiar topics, but because there’s less marginal knowledge you need to capture.

For example, you may notice that I haven’t written prompts about how the ingredients are to be prepared before they’re added to the stock. No need, I feel: roughly chopping vegetables and smashing garlic before using those ingredients as aromatics is the natural inference for most cooks who are serious enough to make stock. But if that’s not a trivial inference for you, prompt away.

Relatedly, the appropriate scale of a “focused” prompt depends on the scale of the concepts you’ve internalized. This particular set of aromatics is so deeply familiar as a group that I’d write prompts which treat it as a unit (“Italian aromatics”) instead of memorizing individual ingredients and quantities.

As you build fluency in increasingly complex concepts, you can write increasingly complex prompts while keeping each focused on what feels like a single detail. In fact, the ability to think in terms of increasingly complex “chunks” appears to be a significant part of what expertise actually is.For a compelling demonstration, see Chase and Simon, Perception in chess (1973), which experimentally demonstrates how chess masters operate in terms of larger chunks. Viewed through this lens, one role for memory systems is to accelerate the process of increasing your effective chunk size in a topic.


Procedural knowledge
Now that we’ve got prompts for the ingredients, let’s look at the steps of the recipe. This is procedural knowledge—knowledge needed to perform specific tasks, more knowing how than knowing what.

In some sense, procedures are lists. So we can start by using the cloze-deletion method we used for the ingredient list:

Q:

???
Bring to a simmer on low heat (this will take about an hour). We use low heat to produce a bright, clean flavor: at higher temperatures, the stock will both taste and look duller.
Lower heat to maintain a bare simmer for an hour and a half.
Strain, wait until cool, then transfer to storage containers.
A. Combine all the ingredients in a large pot.

… and so on, for each of the four steps.

This is an awfully unfocused prompt. It includes many unimportant details which distract from the knowledge you actually intend to retrieve. In my experience, wordy prompts like these tend to dull my concentration and produce vague, distracted answers.

We can improve this prompt somewhat by simply removing words. If necessary, we can add extra prompts to cover any details we removed.

Q:

???
Slowly bring to a simmer
Maintain bare simmer for 90m
Strain, wait until cool, then store
A. Combine all ingredients

This is better. But editing down the procedure helps us make a few observations about this knowledge. First: a few keywords (or word groups) carry the critical details of the procedure: slowly bring to a simmer, then maintain bare simmer for 90m. If you know those four bolded phrases, you basically know this procedure. The other words are just a skeleton. Which brings us to a second observation: the first and fourth steps aren’t worth writing prompts about. If you know what stock is (and we’ll get to that), you know you’re simmering a bunch of ingredients in a pot. When the stock is finished simmering, the final step is common sense. What else would you do?

After highlighting keywords in this way, prompt-writing often feels like playing Jeopardy: can you phrase that in the form of a question? Here’s a revised set of questions which capture my understanding of this procedure.

Q. At what speed should you heat a pot of ingredients for chicken stock?

A. Slowly.

Q. When making chicken stock, when should you lower the heat?

A. After the pot reaches a simmer.

Q. When making chicken stock, what should you do after the pot reaches a simmer?

A. Lower the temperature to a bare simmer.

Q. How long must chicken stock simmer?

A. 90m.

Procedures can often be broken down into keywords like this. What are the important verbs, and when should you move between them? What are the key adjectives, adverbs, subjects, objects?

In our stock recipe, the verbs aren’t very important: “bring,” “lower,” “strain.” You’re cooking ingredients in water at various temperatures, so those actions are obvious. But conditions or heuristics describing when to move between verbs are important: first when the water reaches a simmer, then after ninety minutes passes. And while it’s not worth capturing the fact that you’re heating the pot, the adverb “slowly” is indeed important.

The recipe is quite linear, but more complex procedures may branch, including conditions or special cases which could trigger some alternate path in the flowchart. Such predicate structures are usually worth capturing. If the branching is sufficiently complex, you might consider drawing a flowchart and using that in your prompt.

Is the keyword-based approach better than the list-based approach? That depends on how important the discrete details are and how intuitive they are for you. The keyword-based approach emphasizes the individual knowledge components more strongly, which is a good idea if precision is important. Also, I usually find focused questions like these more pleasant to answer. But if an outline is all you need, then the list approach is probably simpler.

It’s worth noting that in our editing, we’ve left behind a few useful details from the original recipe. Let’s re-add them with separate prompts:

Q. How long should it take to heat a batch of chicken stock (with 2lbs of bones)?

A. About an hour

This knowledge isn’t essential, but “heads-up!”-type information can be quite useful when learning procedures. If you know this detail, you’ll leave yourself enough time when making stock, you won’t be confused when your pot takes forever to heat up, and you might notice that you’re using too high a temperature if the pot boils in fifteen minutes.

Q. Why does Andy’s recipe claim we should prepare chicken stock over low heat?

A. “Brighter, cleaner” flavor.

Explanation-type prompts are especially valuable when studying procedures: they can help you avoid rote learning and build a deeper understanding. Note that in this particular case, we were only able to traverse one level of “why.” Why low heat? A cleaner flavor, says the recipe. Why does low heat produce a cleaner flavor? It doesn’t say. You might find yourself wondering what “brighter” or “cleaner” really even means. Writing this prompt revealed a gap in our understanding: how useful! We could dig into this question, but we’ll choose to keep moving for the moment. We indicate that by explicitly phrasing the answer as tentative, reliant on an external claim.

It’s helpful to add similar caveats to your prompts whenever you’re working with subjective, provisional, or incomplete information. In some sense, most of the prompts we’ve been writing are provisional: other recipes will probably do things somewhat differently. So we could phrase everything more tentatively, but in practice that’s more distracting than it’s worth. It’s usually enough to record where the information came from. Most spaced repetition systems have metadata fields you could use to link these prompts to the original chicken stock recipe.


Exercise: how to store chicken stock?
We’ve written prompts about how to make chicken stock. Now it’s your turn. Use what we’ve learned so far to write prompts representing your understanding of this paragraph on storage notes:

This will yield about 1.5 qt. Chicken stock will keep for a week in the fridge or indefinitely in the freezer. Once chilled, there will be a cap of fat on the stock; skim that off before using the stock, and deploy the fat in place of oil or butter in any savory cooking situation.

You can use this text box as a scratch area. What you write won’t be transmitted or saved.

Here are my prompts:

Click to reveal

Q. 2 lbs of chicken bones yields roughly ??? qt stock

A. 1.5 qt

Q. ??? lbs of chicken bones yields roughly 1.5 qt stock

A. 2 lbs

Q. How long will chicken stock keep in the fridge?

A. A week

Q. How long will chicken stock keep in the freezer?

A. Indefinitely

Q. Once chilled, what should I do before I use a fresh batch of chicken stock?

A. Remove the cap of fat

Q. What should I do with skimmed fat from chicken stock?

A. Keep and use as savory cooking fat

How do these prompts compare to yours? Did I include any details you didn’t cover? Did you cover any details I missed? How do those differences strike you? How does the scope of your prompts compare to these?

What stock is and why it matters: conceptual knowledge
A wheel that can be turned though nothing else moves with it, is not a part of the mechanism.

— Ludwig Wittgenstein, Philosophical Investigations

Now we turn our attention to the first few paragraphs of that recipe. Definitions seem like the simplest things to write prompts for: after all, isn’t that how flashcards are most commonly used in school?

For instance, what about a pair of definition prompts, like this?:

Q. What is stock?

A. A flavorful liquid building block.

Q. Culinary term for flavorful liquid building block?

A. Stock.

Leaving aside quibbles about focus, precision, and consistency, we could probably memorize the verbatim answer to the first question. The reverse definition can help you remember the name for this term, which is often useful. But the ability to parrot these answers isn’t at all the same as knowing what stock is.

Stock is a concept. Knowing the meaning of a concept like “stock” is different from high school flashcard knowledge—for instance knowing that “correre” in Italian means “to run.” To internalize a concept, you need to understand its components and relationships. Your goal is to design a set of prompts which collectively trace the edges of “stock.”

I’ll now introduce some useful lenses for understanding concepts. You won’t necessarily need to use every lens for each concept you encounter. Think of them as a toolkit for identifying elements which seem most important to you. Most of these example prompts are best suited to a novice cook. Experienced cooks usually already know what stock is, though they don’t necessarily know how to make it.

Attributes and tendencies: What makes stock, stock? What’s always, sometimes, and never true of stock?

Q. How are stocks usually made?

A. Simmering flavorful ingredients in water.

Q. Why don’t stocks usually have a distinctive flavor?

A. To make them more versatile.

Similarities and differences: Knowing what stock is requires knowing what relates and distinguishes it from other adjacent concepts.

Q. How is stock different from soup broth?

A. Soup broth has a more complete flavor; stock isn’t meant to stand on its own.

Parts and wholes: What are some examples of stocks? Are there important “sub-concepts” of stocks? Is “stock” a part of some broader category? Visualize a Venn diagram, even if the edges are fuzzy.

Q. Name at least three examples of stock:

A. e.g. chicken, vegetable, mushroom, pork

Q. Stock is rarely served directly; it’s best thought of as a ??? (construction metaphor)

A. Building block.

Causes and effects: What does stock do? What causes it to do that? What doesn’t it do? When is it used?

Q. Why do restaurants use stock as a cooking medium instead of water? (name two reasons)

A. Adds flavor, improves texture.

Q. Stocks are a common base for… (name at least two)

A. e.g. sauces, soups, braises

Q. Restaurants often use stock as a cooking medium where home cooks might use ???.

A. Water

Significance and implications: Why does stock matter? What does it suggest? Make the concept personally meaningful.

Q. What liquid building block explains why simple restaurant dishes are often tastier than home renditions?

A. Stock.

Q. What should I ask myself if I notice I’m using water in savory cooking?

A. “Should I use stock instead?”

This last prompt isn’t stated in the recipe: it’s an example of what might be an understanding of your own. Notice, too, that its aim is more behavioral than intellectual. We’ll have more to say about using prompts to change behavior in our section on how to use chicken stock.


Exercise: what chicken stock is and why it matters
As an exercise in modeling conceptual knowledge, try writing prompts representing your understanding of this paragraph introducing chicken stock and explaining its role:

One of the most ubiquitous and useful stocks is chicken stock. Now, the point of chicken stock isn’t to make everything taste like chicken. When used to prepare vegetables, for example, chicken stock makes them taste more complete, adding background voices which harmonize with the primary flavors. It also adds a luxurious texture because it’s rich in gelatin extracted from the chicken bones. Chicken stock takes only a few minutes of active time to make, and in a typical kitchen, it’s basically free: the primary ingredient is chicken bones, which you can naturally accumulate in your freezer if you cook chicken regularly.

You can use this text box as a scratch area. What you write won’t be transmitted or saved.

Here are some prompts I might write:

Click to reveal

Q. Chicken stock doesn’t make vegetables taste like chicken; it makes them taste more ??? (according to Andy’s recipe)

A. “complete”

Q. Chicken stock makes vegetables taste “more complete” by adding ??? which ??? with the primary flavors (music metaphor)

A. supporting voices; harmonize

Q. Besides improving flavor, chicken stock adds a luxurious ??? to dishes

A. texture

Q. Flavor and diet issues aside, why use chicken stock instead of vegetable or mushroom stocks?

A. Chicken stock has gelatin, which creates a luxurious texture

Q. Why is chicken stock economical?

A. Its main ingredient (bones) accumulates for free if you cook with chicken

Q. What should I do with the carcass of a roast chicken?

A. Freeze it and make chicken stock

There was one prompt which I found I wanted to write but couldn’t, at least while using only the information in the recipe:

Q. When to use chicken stock versus other types of meat stock?

A. ???

Prompt-writing can helpfully reveal such gaps in our understanding. You don’t need to stick with one resource: follow your nose; Google around; consult other references. Even if you don’t decide to follow up on the missing information immediately, you can guide future exploration by sensitizing yourself to feelings of curiosity and gaps in understanding.

How do these prompts compare to yours? Did I include any details you didn’t cover? Did you cover any details I missed? How do those differences strike you? How does the scope of your prompts compare to these?

You’ll notice that I don’t necessarily use all the lenses I introduced in the previous section. For instance, I didn’t feel there were any useful part/whole prompts to ask. And the most important attribute of chicken stock is that it’s made with chicken, but it would be silly to ask about that.

Using chicken stock: open lists and salience prompts
There’s no sense in making a batch of chicken stock unless you know how to use it. The recipe includes a list of suggestions. How might we create understanding around this type of knowledge?

Open lists
We learned some techniques for representing lists when we were writing prompts for our recipe’s ingredients. Could we use a similar technique here?

Q. Things to do with chicken stock:

???
wilt and steam hearty greens
make purée soups
deglaze pans
A. Cook grains in it

This prompt doesn’t work. Anything could reasonably go in that first slot. You might notice, too, that this list feels so much more arbitrary than the list of ingredients in chicken stock. The difference is that this is an open list. You don’t really mean to memorize this exact list, though it might be useful to name a few members on demand. No, if you keep cooking, you’ll be adding to this list your whole life. By contrast, the list of ingredients in our recipe has a fixed set of members: it’s a closed list.

I think of closed lists as a complex fact, almost an equation:

radius of earth = 6,371 km

chicken stock ingredients = onions, carrots, celery, garlic, parsley.

In fact, if you’re an experienced cook, you probably think of the ingredients in chicken stock as an open list—if that’s true, it’d be better to represent them that way! This is a common fate for closed lists in human-scale concepts.I like to think of open lists like tags—like the tags you might use in a system for digital bookmarks. My mental filing cabinet has a tag called “way to use chicken stock,” and I’ve fastened that tag to some notes about making purée soups.

When I encode this type of knowledge, I find three types of prompts consistently helpful. First I write prompts focused on each of the tagged items, linking from the instance to the tag. Then I might separately write prompts about the tag itself, perhaps inspired by patterns I notice in its instances. Finally, I often write a prompt which fuzzily links from the tag to its instances by asking for examples.

For example, this prompt links an instance to the tag:

Q. When puréeing vegetables to make soup, how can I produce a richer flavor without adding fat?

A. Thin the purée with chicken stock instead of water.

After we’ve written several prompts like this, a prompt about a pattern in the tag might suggest itself:

Q. What should I ask myself if I notice I’m using water in savory cooking?

A. “Should I use stock instead?”

It’s often useful to be able to summon examples of a tag on demand. We can write a prompt which fuzzily links the tag to instances:

Q. Name two ways you might use chicken stock.

A. e.g. cooking grains, steaming hearty greens, making purée soups, deglazing pans

This type of prompt is easy to write, so it’s tempting to write something similar and be done with it. But prompts like this usually don’t work well without other prompts supporting it. You’ll probably find yourself giving the same examples each time. In the absence of additional prompts, you’ll likely forget about the other instances. If you do change your answer each time, the prompt won’t satisfy the consistency property we’ve introduced, and interference effects may leave your memory unreliable without other supporting prompts.

When you’ve just learned a particularly open-ended concept—one which could apply to many instances—you can turn example-generating prompts like the one above into creative prompts like this one:

Q. Name a vegetable purée soup which you might try making with chicken stock (give an answer you haven’t given before)

A. e.g. potato, parsnip, celeriac, sunchoke, salsify, squash, carrot, pepper, lentil…

The novelty admonition is an interesting trick: “give an answer you haven’t given before.” Sure, after a year or two, maybe you’ll re-use a vegetable without realizing it. That’s fine. But note that you probably can’t write a prompt like this one about contexts to use chicken stock, unless you have enough prior experience to generate plenty of different answers.

This isn’t really a retrieval prompt anymore. Creative prompts are more like a textbook exercise, asking you to apply what you’ve learned in a new way. Unlike the other prompts we’ve seen, the goal here is to avoid retrieving an answer from memory: you’re meant to think creatively for a few moments. Since your answer’s different each time, retrieval practice won’t consistently reinforce your memory of any particular response. Instead, it will reinforce whatever knowledge you consistently use when generating an answer. Your novel responses may also make meaningful associations which strengthen your memory through elaborative encoding. And those associations may be particularly sticky because ofSee Slamecka and Graf, The Generation Effect: Delineation of a Phenomenon (1978). another memory phenomenon called the generation effect: you remember information better when you generated it yourself.

Michael Nielsen and I have experimented with application-focused spaced repetition prompts in Quantum mechanics distilled, but we don’t yet feel we understand them.I’ve described a few mechanisms which creative prompts might employ, but I should be clear that these prompts are much less well understood than the retrieval-focused prompts we’ve examined so far. What specific effects, if any, do such tasks have on our memory and understanding? Through what mechanisms? In what situations and with what properties are they most useful? What repetition schedule should be used for such tasks? These remain open research questions.


Salience prompts and the Baader-Meinhof phenomenon
Besides their impact on memory and understanding, many of the prompts we’ve been discussing about have another important effect: they keep you in contact with an idea over time.

Have you ever heard about something for the first time, then suddenly noticed it everywhere? Maybe you learn an unusual word like “mellifluous,” then spot it several times in the following days. In 1994 a pseudonymous internet commenter dubbed this the Baader-Meinhof Phenomenon (after being surprised to see two independent references to that terrorist group within a day). Stanford linguistics professor Arnold Zwicky suggests that this effect is a kind of selective attention: new ideas are particularly salient, so we notice them more readily. They haven’t really become more common—they just seem that way.

Sometimes this effect isn’t helpful. You can probably remember a time when a friend learned a new idea, and then everything became an (inappropriate) nail for their new hammer. But to really internalize a new idea, you need to bring it into your life and make meaning with it. In particular, if it’s a new skill, you probably haven’t really understood it until you’ve put it into practice several times on your own.

Salience typically fades over time. If you don’t soon have a chance to connect that new idea to something meaningful in your life, you may stop noticing opportunities so readily. The dynamic seems similar to the problem of forgetting knowledge over time. So one valuable use for spaced repetition prompts is to keep ideas salient, top of mind, over longer periods of time. Gwern Branwen has pointed out** In private communication. that such prompts are effectively trying to extend the Baader-Meinhof phenomenon and control it for a purpose.

We’ve already written a few prompts which focus on salience:

Q. What should I ask myself if I notice I’m using water in savory cooking?

A. “Should I use stock instead?”

Q. What should I do with the carcass of a roast chicken?

A. Freeze it and make chicken stock

Q. Name a vegetable purée soup which you might try making with chicken stock (give an answer you haven’t given before)

A. e.g. potato, parsnip, celeriac, sunchoke, salsify, squash, carrot, pepper, lentil…

The point of those prompts isn’t really to “know” those answers intellectually. It’s to cue certain ideas, which in turn may prompt new thoughts or create new behaviors. Viewed in this way, the point of repeating these prompts over time is to keep the relevant ideas salient until they have a chance to connect to something meaningful in your life. As economist Brad DeLong suggests, review sessions are surprisingly like a secular catechism.

Many of the Orbit prompts in this guide are of this kind. They’re meant to keep you in contact with these ideas until you can make sense of them as you write your own prompts. Odd as it may seem, I often write such prompts about my own ideas in the course of my creative work. They help me muse on an inkling or question over weeks and months, until it can hopefully grow into something more. This is one way prompt-writing can create understanding which extends beyond simply capturing knowledge from a text.

It’s often helpful to phrase salience prompts around contexts where those ideas might be meaningful in your life. For example, many cooks usually buy individual parts of a chicken instead of whole birds. Perhaps you’d like to start buying whole chickens so that you can use the bones for stock. This prompt demonstrates how you might target a specific situation:

Q. To help keep my freezer full of chicken stock, I’ll make sure to ??? instead of ??? when buying chicken.

A. buy whole birds; buying parts

This example helps illustrate a broader issue. Just because you can answer a factual question about an idea, that doesn’t mean the idea will spontaneously occur to you when it’s useful.This is one facet of a broad problem in educational psychology called transfer of learning: how do people transfer what they learn in one situation to a different one? I don’t have a well-grounded understanding of the difference, but in my experience, context-laden prompts (like this last example) help the leap from theory to practice. I suspect this is another reason it’s important to densely connect new ideas to old ones, as we did in the conceptual knowledge section: roughly speaking, more connections means more opportunities to trigger new knowledge.

What makes a spaced repetition prompt most likely to change your behavior or prompt new thoughts? What schedule should one use for repeating such prompts? If the objective isn’t memory, the schedule shouldn’t be tuned by “forgotten” and “remembered” buttons—so what should replace them? These remain open questions.


Exercise: variations
The chicken stock recipe includes a paragraph on variations, which are in some sense an open list. Write prompts representing your understanding of the knowledge in this paragraph:

For a more French flavor profile, replace the celery with leeks and add any/all of bay leaves, black peppercorns, and thyme. For a deeper flavor, roast the bones and vegetables first to make what’s called a “brown chicken stock” (the original recipe is for a “white chicken stock,” which is more delicately flavored, making it versatile but less intense).

You can use this text box as a scratch area. What you write won’t be transmitted or saved.

Writing prompts, in practice
Iterative prompt-writing
This guide aspires to demonstrate a wide variety of techniques, so I’ve deliberately analyzed the chicken stock recipe quite exhaustively. But in practice, if you were examining a recipe for the first time, I certainly wouldn’t recommend writing dozens of prompts at once like we’ve done here. If you try to analyze everything you read so comprehensively, you’re likely to waste time and burn yourself out.

Those issues aside, it’s hard to write good prompts on your first exposure to new ideas. You’re still developing a sense of which details are important and which are not—both objectively, and to you personally. You likely don’t know which elements will be particularly challenging to remember (and hence worth extra reinforcement). You may not understand the ideas well enough to write prompts which access their “essence”, or which capture subtle implications. And you may need to live with new ideas for a while before you can write prompts which connect them vibrantly with whatever really matters to you.

All this suggests an iterative approach.

Say you’re reading an article that seems interesting. Try setting yourself an accessible goal: on your first pass, aim to write a small number of prompts (say, 5-10) about whatever seems most important, meaningful, or useful.

I find that such goals change the way I read even casual texts. When first adopting spaced repetition practice, I felt like I “should” write prompts about everything. This made reading a chore. By contrast, it feels quite freeing to aim for just a few key prompts at a time.As Michael Nielsen notes, similar lightweight prompt-writing goals can enliven seminars, professional conversations, events, and so on. I read a notch more actively, noticing a tickle in the back of my mind: “Ooh, that’s a juicy bit! Let’s get that one!”

If the material is fairly simple, you may be able to write these prompts while you read. But for texts which are challenging or on an unfamiliar topic, it may be too disruptive to switch back and forth. In such cases it’s better to highlight or make note of the most important details. Then you can write prompts about your understanding of those details in a batch at the end or at a suitable stopping point. For these tougher topics, I find it’s best to focus initially on prompts about basic details you can build on: raw facts, terms, notation, etc.

Books are more complicated: there are many kinds of books and many ways to read them. This is true of articles, too, of course, but books amplify the variance. For one thing, you’re less likely to read a book linearly than an article. And, of course, they’re longer, so a handful of prompts will rarely suffice. The best prompt-writing approach will depend on how and why you’re reading the book, but in general, if I’m trying to internalize a non-fiction book, I’ll often begin by aiming to write a few key prompts on my first pass through a chapter or major section.

For many resources, one pass of prompt-writing is all that’s worth doing, at least initially. But if you have a rich text which you’re trying to internalize thoroughly, it’s often valuable to make multiple passes, even in the first reading session. That doesn’t necessarily mean doubling down on effort: just write another handful of apparently-useful prompts each time. For a vivid account of this process in mathematics, see Michael Nielsen, Using spaced repetition systems to see through a piece of mathematics (2019).With each iteration, you’ll likely find yourself able to understand (and write prompts for) increasingly complex details. You may notice your attention drawn to patterns, connections, and bigger-picture insights. Even better: you may begin to focus on your own observations and questions, rather than those of the author. But it’s also important to notice if you feel yourself becoming restless. There’s no deep virtue in writing a prompt about every detail. In fact, it’s much more important to remain responsive to your sense of curiosity and interest.

Piotr Wozniak, a pioneer of spaced repetition, has been developing a system he calls incremental reading which attempts to actively support this kind of iterative, incremental prompt writing.If you notice a feeling of duty or completionism, remind yourself that you can always write more prompts later. In fact, they’ll probably be better if you do: motivated by something meaningful, like a new connection or a gap in your understanding.

Let’s consider our chicken stock recipe again for a moment. If I were an aspiring cook who had never heard of stock before, I’d probably write a few prompts about what stock is and why it matters: those details seem useful beyond the scope of this single recipe, and they connect to happy dining experiences I’ve had. That’s probably all I’d do until I actually made a batch of stock for myself. At that point, I’d know which steps were obvious and which made me consult the recipe. If I found I wanted to make stock again, I’d write another batch of prompts to recall details like ingredient ratios and times. I’d try to notice places where I found myself straining, vaguely aware that I’d “read something about this” but unsure of the details. As I used my first batch of stock in subsequent dishes, I might then write prompts about those experiences. And so on.


Litmus tests
While you’re drafting prose, a spell checker and grammar checker can help you avoid some simple classes of error. Such tools don’t yet exist for prompt-writing, so it’s helpful to collect simple tests which can serve a similar function.

False positives: How might you produce the correct answer without really knowing the information you intend to know?

Discourage pattern matching. If you write a long question with unusual words or cues, you might eventually memorize the shape of that question and learn its corresponding answer—not because you’re really thinking about the knowledge involved, but through a mechanical pattern association. Cloze deletions seem particularly susceptible to this problem, especially when created by copying and editing passages from texts. This is best avoided by keeping questions short and simple.

Avoid binary prompts. Questions which ask for a yes/no or this/that answer tend to require little effort and produce shallow understanding. I find I can often answer such questions without really understanding what they mean. Binary prompts are best rephrased as more open-ended prompts. For instance, the first of these can be improved by transforming it into the second:

Q. Does chicken stock typically make vegetable dishes taste like chicken?

A. No.

Q. How does chicken stock affects the flavor of vegetable dishes? (according to Andy’s recipe)

A. It makes them taste more “complete.”

Improving a binary prompt often involves connecting it to something else, like an example or an implication. The lenses in the conceptual knowledge section are useful for this.

False negatives: How might you know the information the prompt intends to capture but fail to produce the correct answer? Such failures are often caused by not including enough context.

It’s easy to accidentally write a question which has correct answers besides the one you intend. You must include enough context that reasonable alternative answers are clearly wrong, while not including so much context that you encourage pattern matching or dilute the question’s focus.

For example, if you’ve just read a recipe for making an omelette, it might feel natural to ask: “What’s the first step to cook an omelette?” The answer might seem obvious relative to the recipe you just read: step one is clearly “heat butter in pan”! But six months from now, when you come back to this question, there are many reasonable answers: whisk eggs; heat butter in a pan; mince mushrooms for filling; etc.

One solution is to give the question extremely precise context: “What’s the first step in the Bon Appetit Jun ’18 omelette recipe?” But this framing suggests the knowledge is much more provincial than it really is. When possible, general knowledge should be expressed generally, so long as you can avoid ambiguity. This may mean finding another angle on the question; for instance: “When making an omelette, how must the pan be prepared before you add the eggs?”

False negatives often feel like the worst nonsense from school exams: “Oh, yes, that answer is correct—but it’s not the one we were looking for. Try again?” Soren Bjornstad points out that a prompt which fails to exclude alternative correct answers requires that you also memorize “what the prompt is asking.”


Revising prompts over time
It’s often tough to diagnose issues with prompts while you’re writing them. Problems may become apparent only upon review, and sometimes only once a prompt’s repetition interval has grown to many months. Prompt-writing involves long feedback loops. So just as it’s important to write prompts incrementally over time, it’s also important to revise prompts incrementally over time, as you notice problems and opportunities.

In your review sessions, be alert to feeling an internal “sigh” at a prompt. Often you’ll think: “oh, jeez, this prompt—I can never remember the answer.” Or “whenever this prompt comes up, I know the answer, but I don’t really understand what it means.” Listen for those reactions and use them to drive your revision. To avoid disrupting your review session, most spaced repetition systems allow you to flag a prompt as needing revision during a review. Then once your session is finished, you can view a list of flagged prompts and improve them.

The analogy to sentences is drawn from Matuschak and Nielsen, How can we develop transformative tools for thought? (2019).Learning to write good prompts is like learning to write good sentences. Each of these skills sometimes seems trivial, but each can be developed to a virtuosic level. And whether you’re writing prompts or writing sentences, revision is a holistic endeavor. When editing prose, you can sometimes focus your attention on a single sentence. But to fix an awkward line, you may find yourself merging several sentences together, modifying your narrative devices, or changing broad textual structures. I find a similar observation applies to editing spaced repetition prompts. A prompt can sometimes be improved in isolation, but as my understanding shifts I’ll often want to revise holistically—merge a few prompts here, reframe others there, split these into finer details. If you’ve attempted the exercises, you may notice that it’s easier to revise across question boundaries when composing multiple questions in the same text field. As an experiment, I’ve written almost all new prompts in 2020 as simple “Q. / A.” lines (like the examples in this guide) embedded in plaintext notes, using an old-fashioned text editor instead of a dedicated interface. I find I prefer this approach in most situations. In the future, I may release tools which allow others to write prompts in this way.Unfortunately, most spaced repetition interfaces treat each prompt as a sovereign unit, which makes this kind of high-level revision difficult. It’s as if you’re being asked to write a paper by submitting sentence one, then sentence two, and so on, revising only by submitting a request to edit a specific sentence number. Future systems may improve upon this limitation, but in the meantime, I’ve found I can revise prompts more effectively by simply keeping a holistic aspiration in mind.

In this guide, I’ve analyzed an example quite exhaustively to illustrate a wide array of principles, and I’ve advised you to write more prompts than might feel natural. So I’d like to close by offering a contrary admonition.

I believe the most important thing to “optimize” in spaced repetition practice is the emotional connection to your review sessions and their contents. It’s worth learning how to create prompts which effectively represent many different kinds of understanding, but a prompt isn’t worth reviewing just because it satisfies all the properties I’ve described here. If you find yourself reviewing something you don’t care about anymore, you should act. Sometimes upon reflection you’ll remember why you cared about the idea in the first place, and you can revise the prompt to cue that motivation. But most of the time the correct way to revise such prompts is to delete them.

Another way to approach this advice is to think about its reverse: what material should you write prompts about? When are these systems worth using? Many people feel paralyzed when getting started with spaced repetition, intrigued but unsure where it applies in their life. Others get started by trying to memorize trivia they feel they “should” know, like the names of all the U.S. presidents. Boredom and abandonment typically ensue. The best way to begin is to use these systems to help you do something that really matters to you—for example, as a lever to more deeply understand ideas connected to your core creative work. With time and experience, you’ll internalize the benefits and costs of spaced repetition, which may let you identify other useful applications (like I did with cooking). If you don’t see a way to use spaced repetition systems to help you do something that matters to you, then you probably shouldn’t bother using these systems at all.


Further reading
These resources have been especially useful to me as I’ve developed an understanding of how to write good prompts:

Piotr Wozniak’s Effective learning: Twenty rules of formulating knowledge and the more detailed Knowledge structuring and representation in learning based on active recall tackle the same topic as this guide from a different perspective.
Michael Nielsen’s Augmenting Long-term Memory: a thorough review of how spaced repetition works and why you should care; more details on how to practically integrate prompt-writing into your reading practices, particularly when reading academic literature; notes on creative applications; and much more.
Michael Nielsen’s Using spaced repetition systems to see through a piece of mathematics demonstrates how to iteratively deepen one’s understanding of a piece of mathematics, using spaced repetition prompts as a lever.
For more perspectives on this and related topics, see:

Soren Bjornstad’s series on memory systems helpfully covers many practical topics in maintaining a prompt library, including some advice on prompt-writing.
Nicky Case’s How To Remember Anything Forever-ish introduces spaced repetition and covers some prompt-writing techniques through delightful illustrations.
How can we develop transformative tools for thought? (from Michael Nielsen and me) discusses the challenges of prompt-writing with particular focus on the “mnemonic medium,” which involves embedding prompts in narrative prose.
