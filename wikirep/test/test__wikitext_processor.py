#!/usr/bin/python
# -*- coding: utf-8 -*-
'''
Created on Nov 28, 2012

@author: inesmeya
'''
import unittest

class Test(unittest.TestCase):

    def test__TextClean(self):
        import parsers.wikitext_processor as wp
        text = """
Knowledge acquisition involves complex [[Cognition|cognitive]] processes: perception, communication, association and reasoning; while knowledge is also said to be related to the capacity of ''acknowledgment'' in human beings.&lt;ref&gt;Stanley Cavell, &quot;Knowing and Acknowledging,&quot; ''Must We Mean What We Say?'' (Cambridge University Press, 2002), 238–266.&lt;/ref&gt;

==Theories of knowledge==
[[File:Knowledge-Reid-Highsmith.jpeg|thumb|left|[[Robert Reid (painter)|Robert Reid]], ''Knowledge'' (1896). [[Thomas Jefferson Building]], Washington, D.C.]]
{{see also|Epistemology}}
{{cquote2
|The eventual demarcation of philosophy from science was made possible by the notion that philosophy's core was &quot;theory of knowledge,&quot; a theory distinct from the sciences because it was their ''foundation''… Without this idea of a &quot;theory of knowledge,&quot; it is hard to imagine what &quot;philosophy&quot; could have been in the age of modern science.|[[Richard Rorty]]|''Philosophy and the Mirror of Nature''}}&lt;/blockquote&gt;

The  definition of knowledge is a matter of on-going [[debate]] among [[philosopher]]s in the field of [[epistemology]]. The classical definition, described but not ultimately endorsed by [[Plato]],&lt;ref&gt;In Plato's ''[[Theaetetus (dialogue)|Theaetetus]]'', Socrates and Theaetetus discuss three definitions of ''knowledge'': knowledge as nothing but perception, knowledge as true judgment, and, finally, knowledge as a true judgment with an account. Each of these definitions is shown to be unsatisfactory.&lt;/ref&gt; specifies that a [[statement (logic)|statement]] must meet three [[wikt:criterion|criteria]] in order to be considered knowledge: it must be [[theory of justification|justified]], [[truth|true]], and [[belief|believed]]. Some claim that these conditions are not sufficient, as [[Gettier case]] examples allegedly demonstrate. There are a number of alternatives proposed, including [[Robert Nozick]]'s arguments for a requirement that knowledge 'tracks the truth' and [[Simon Blackburn|Simon Blackburn's]] additional requirement that we do not want to say that those who meet any of these conditions 'through a defect, flaw, or failure' have knowledge. [[Richard Kirkham]] suggests that our definition of knowledge requires that the evidence for the belief necessitates its truth.&lt;ref&gt;http://www.centenary.edu/attachments/philosophy/aizawa/courses/epistemologyf2008/kirkham1984.pdf&lt;/ref&gt;

In contrast to this approach, [[Ludwig Wittgenstein|Wittgenstein]] observed, following [[Moore's paradox]], that one can say &quot;He believes it, but it isn't so&quot;, but not &quot;He knows it, but it isn't so&quot;.&lt;ref&gt;[[Ludwig Wittgenstein]], ''[[On Certainty]]'', remark 42&lt;/ref&gt; He goes on to argue that these do not correspond to distinct mental states, but rather to distinct ways of talking about conviction. What is different here is not the mental state of the speaker, but the activity in which they are engaged. For example, on this account, to ''know'' that the kettle is boiling is not to be in a particular state of mind, but to perform a particular task with the statement that the kettle is boiling. Wittgenstein sought to bypass the difficulty of definition by looking to the way &quot;knowledge&quot; is used in natural languages. He saw knowledge as a case of a [[family resemblance]]. Following this idea, &quot;knowledge&quot; has been reconstructed as a cluster concept that points out relevant features but that is not adequately captured by any definition.&lt;ref&gt;Gottschalk-Mazouz, N. (2008): &quot;Internet and the flow of knowledge&quot;, in: Hrachovec, H.; Pichler, A. (Hg.): Philosophy of the Information Society. Proceedings of the 30. International Ludwig Wittgenstein Symposium Kirchberg am Wechsel, Austria 2007. Volume 2, Frankfurt, Paris, Lancaster, New Brunswik: Ontos, S. 215–232. http://www.uni-stuttgart.de/philo/fileadmin/doc/pdf/gottschalk/ngm-internetflow-2008.pdf&lt;/ref&gt;

==Communicating knowledge==
[[File:Los portadores de la antorcha.jpg|thumb|''Los portadores de la antorcha'' &lt;br&gt; Sculpture by [[Anna Hyatt Huntington]] about the transmission of knowledge from one generation to the next &lt;br&gt;([[Complutense University of Madrid|Ciudad Universitaria, Madrid, Spain]])]]
[[Symbolic linguistic representation|Symbolic representation]]s can be used to indicate meaning and can be thought of as a dynamic process. Hence the transfer of the symbolic representation can be viewed as one [[wikt:ascription|ascription]] process whereby knowledge can be transferred. Other forms of communication include observation and imitation, verbal exchange, and audio and video recordings. Philosophers of language and [[semioticians]] construct and analyze theories of knowledge transfer or communication.{{Citation needed|date=September 2007}}
"""
        
        clean_text = wp.clean_wiki_text_text_only(text)
        print clean_text
        #links_gen = wp.get_links(text)
        #for link in links_gen:
        #   print link


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
    
    
text = """
        {{other uses}}
{{pp-move|small=yes}}
[[File:Efez Celsus Library 5 RB.jpg|thumb|upright|Personification of knowledge ([[Greek language|Greek]] ''Επιστημη'', [[Episteme]]) in [[Celsus Library]] in [[Ephesus]], Turkey.]]
'''Knowledge''' is a familiarity with someone or something, which can include [[fact]]s, [[information]],  [[description]]s,  or [[skills]] acquired through [[experience]] or [[education]]. It can refer to the theoretical or practical understanding of a subject. It can be implicit (as with practical skill or expertise) or explicit (as with the theoretical understanding of a subject); it can be more or less formal or systematic.&lt;ref&gt;http://oxforddictionaries.com/view/entry/m_en_us1261368#m_en_us1261368&lt;/ref&gt; In [[philosophy]], the study of knowledge is called [[epistemology]]; the philosopher [[Plato]] famously defined knowledge as &quot;[[justified true belief]].&quot; However, no single agreed upon definition of knowledge exists, though there are numerous theories to explain it. The following quote from Bertrand Russell's &quot;Theory of Knowledge&quot; illustrates the difficulty in defining knowledge: &quot;The question how knowledge should be defined is perhaps the most important and difficult of the three with which we shall deal. This may seem surprising: at first sight it might be thought that knowledge might be defined as belief which is in agreement with the facts. The trouble is that no one knows what a belief is, no one knows what a fact is, and no one knows what sort of agreement between them would make a belief true. Let us begin with belief.&quot;

Knowledge acquisition involves complex [[Cognition|cognitive]] processes: perception, communication, association and reasoning; while knowledge is also said to be related to the capacity of ''acknowledgment'' in human beings.&lt;ref&gt;Stanley Cavell, &quot;Knowing and Acknowledging,&quot; ''Must We Mean What We Say?'' (Cambridge University Press, 2002), 238–266.&lt;/ref&gt;

==Theories of knowledge==
[[File:Knowledge-Reid-Highsmith.jpeg|thumb|left|[[Robert Reid (painter)|Robert Reid]], ''Knowledge'' (1896). [[Thomas Jefferson Building]], Washington, D.C.]]
{{see also|Epistemology}}
{{cquote2
|The eventual demarcation of philosophy from science was made possible by the notion that philosophy's core was &quot;theory of knowledge,&quot; a theory distinct from the sciences because it was their ''foundation''… Without this idea of a &quot;theory of knowledge,&quot; it is hard to imagine what &quot;philosophy&quot; could have been in the age of modern science.|[[Richard Rorty]]|''Philosophy and the Mirror of Nature''}}&lt;/blockquote&gt;

The  definition of knowledge is a matter of on-going [[debate]] among [[philosopher]]s in the field of [[epistemology]]. The classical definition, described but not ultimately endorsed by [[Plato]],&lt;ref&gt;In Plato's ''[[Theaetetus (dialogue)|Theaetetus]]'', Socrates and Theaetetus discuss three definitions of ''knowledge'': knowledge as nothing but perception, knowledge as true judgment, and, finally, knowledge as a true judgment with an account. Each of these definitions is shown to be unsatisfactory.&lt;/ref&gt; specifies that a [[statement (logic)|statement]] must meet three [[wikt:criterion|criteria]] in order to be considered knowledge: it must be [[theory of justification|justified]], [[truth|true]], and [[belief|believed]]. Some claim that these conditions are not sufficient, as [[Gettier case]] examples allegedly demonstrate. There are a number of alternatives proposed, including [[Robert Nozick]]'s arguments for a requirement that knowledge 'tracks the truth' and [[Simon Blackburn|Simon Blackburn's]] additional requirement that we do not want to say that those who meet any of these conditions 'through a defect, flaw, or failure' have knowledge. [[Richard Kirkham]] suggests that our definition of knowledge requires that the evidence for the belief necessitates its truth.&lt;ref&gt;http://www.centenary.edu/attachments/philosophy/aizawa/courses/epistemologyf2008/kirkham1984.pdf&lt;/ref&gt;

In contrast to this approach, [[Ludwig Wittgenstein|Wittgenstein]] observed, following [[Moore's paradox]], that one can say &quot;He believes it, but it isn't so&quot;, but not &quot;He knows it, but it isn't so&quot;.&lt;ref&gt;[[Ludwig Wittgenstein]], ''[[On Certainty]]'', remark 42&lt;/ref&gt; He goes on to argue that these do not correspond to distinct mental states, but rather to distinct ways of talking about conviction. What is different here is not the mental state of the speaker, but the activity in which they are engaged. For example, on this account, to ''know'' that the kettle is boiling is not to be in a particular state of mind, but to perform a particular task with the statement that the kettle is boiling. Wittgenstein sought to bypass the difficulty of definition by looking to the way &quot;knowledge&quot; is used in natural languages. He saw knowledge as a case of a [[family resemblance]]. Following this idea, &quot;knowledge&quot; has been reconstructed as a cluster concept that points out relevant features but that is not adequately captured by any definition.&lt;ref&gt;Gottschalk-Mazouz, N. (2008): &quot;Internet and the flow of knowledge&quot;, in: Hrachovec, H.; Pichler, A. (Hg.): Philosophy of the Information Society. Proceedings of the 30. International Ludwig Wittgenstein Symposium Kirchberg am Wechsel, Austria 2007. Volume 2, Frankfurt, Paris, Lancaster, New Brunswik: Ontos, S. 215–232. http://www.uni-stuttgart.de/philo/fileadmin/doc/pdf/gottschalk/ngm-internetflow-2008.pdf&lt;/ref&gt;

==Communicating knowledge==
[[File:Los portadores de la antorcha.jpg|thumb|''Los portadores de la antorcha'' &lt;br&gt; Sculpture by [[Anna Hyatt Huntington]] about the transmission of knowledge from one generation to the next &lt;br&gt;([[Complutense University of Madrid|Ciudad Universitaria, Madrid, Spain]])]]
[[Symbolic linguistic representation|Symbolic representation]]s can be used to indicate meaning and can be thought of as a dynamic process. Hence the transfer of the symbolic representation can be viewed as one [[wikt:ascription|ascription]] process whereby knowledge can be transferred. Other forms of communication include observation and imitation, verbal exchange, and audio and video recordings. Philosophers of language and [[semioticians]] construct and analyze theories of knowledge transfer or communication.{{Citation needed|date=September 2007}}

While many would agree that one of the most universal and significant tools for the transfer of knowledge is writing (of many kinds), argument over the usefulness of the written word exists nonetheless, with some scholars skeptical of its impact on societies. In his collection of essays ''[[Technopoly: the Surrender of Culture to Technology|Technopoly]]'' Neil Postman demonstrates the argument against the use of writing through an excerpt from Plato's work ''[[Phaedrus (dialogue)|Phaedrus]]'' (Postman, Neil (1992) ''Technopoly'', Vintage, New York, pp 73). In this excerpt the scholar [[Socrates]] recounts the story of Thamus, the Egyptian king and Theuth the inventor of the written word. In this story, Theuth presents his new invention &quot;writing&quot; to King Thamus, telling Thamus that his new invention &quot;will improve both the wisdom and memory of the Egyptians&quot; (Postman, Neil (1992) Technopoly, Vintage, New York, pp 74). King Thamus is skeptical of this new invention and rejects it as a tool of recollection rather than retained knowledge. He argues that the written word will infect the Egyptian people with fake knowledge as they will be able to attain facts and stories from an external source and will no longer be forced to mentally retain large quantities of knowledge themselves (Postman, Neil (1992) ''Technopoly'', Vintage, New York,pp 74).

Andrew Robinson also highlights, in his work ''The Origins of Writing'', the possibility for writing to be used to spread false information and therefore the ability of the written word to decrease social knowledge (Robinson, Andrew (2003) ''The Origins of Writing'' in Crowley and Heyer (eds) Communication in History: Technology, Culture, Society, Boston pp 34). People are often internalizing new information which they perceive to be knowledge but in reality fill their minds with false knowledge.  

The above points are moot in the modern world. Verbal communication lends itself to the spread of falsehoods much more so than written, as there is no record of exactly what was said or who originally said it (usually neither the source nor the content can be verified). Gossip and rumors are common examples.  As to value of writing, the extent of human knowledge is now so great that it is only possible to record it and to communicate it through writing. Major libraries today can have millions of books of knowledge (in addition to works of fiction). It is only recently that audio and video technology for recording knowledge have become available and the use of these still requires replay equipment and electricity.  Verbal teaching and handing down of knowledge is limited to those few who would have contact with the transmitter person - far too limited for today's world.  Writing is still the most available and most universal of all forms of recording and transmitting knowledge.  It stands unchallenged as mankind's primary technology of knowledge transfer down through the ages and to all cultures and languages of the world.

==Situated knowledge==
Situated knowledge is knowledge specific to a particular situation.&lt;ref&gt;Haraway, Donna 1998. ''Situated Knowledges: The Science Question in Feminism and the Privilege of Partial Perspective''.&lt;/ref&gt;

Some methods of generating knowledge, such as [[trial and error]], or learning from [[experience]], tend to create highly situational knowledge. One of the main attributes of the [[scientific method]] is that the theories it generates are much less situational than knowledge gained by other methods.{{Citation needed|date=September 2007}}
Situational knowledge is often embedded in language, culture, or traditions.{{Citation needed|date=September 2007}}

Knowledge generated through experience is called knowledge &quot;a posteriori&quot;, meaning afterwards. The pure existence of a term like &quot;a posteriori&quot; means this also has a counterpart. In this case that is knowledge &quot;a priori&quot;, meaning before. The knowledge prior to any experience means that there are certain &quot;assumptions&quot; that one takes for granted. For example if you are being told about a [[chair]] it is clear to you that the chair is in [[space]], that it is [[three dimensional space|3D]]. This knowledge is not knowledge that one can &quot;forget&quot;, even someone suffering from amnesia experiences the world in 3D. See also: ''[[A priori and a posteriori (philosophy)|a priori and a posteriori]]''.{{Citation needed|date=September 2007}}

==Partial knowledge==
One discipline of [[epistemology]] focuses on [[dispersed knowledge|partial knowledge]]. In most cases, it is not possible to understand an information domain exhaustively; our knowledge is always ''incomplete'' or partial. Most real problems have to be solved by taking advantage of a partial understanding of the problem context and problem data, unlike the typical math problems one might solve at school, where all data is given and one is given a complete understanding of formulas necessary to solve them.{{Citation needed|date=September 2007}}

This idea is also present in the concept of [[bounded rationality]] which assumes that in real life situations people often have a limited amount of information and make decisions accordingly.

==Scientific knowledge==

The development of the [[scientific method]] has made a significant contribution to how knowledge is acquired. To be termed scientific, a method of [[inquiry]] must be based on gathering [[observable]] and [[Measurement|measurable]] [[evidence]] subject to specific principles of [[reasoning]] and experimentation.&lt;ref&gt;
&quot;[4] Rules for the study of [[natural philosophy]]&quot;, {{harvnb|Newton|1999|pp=794–6}}, from the [[General Scholium]], which follows Book '''3''', ''The System of the World''.  
&lt;/ref&gt; The scientific method consists of the collection of [[data]] through [[observation]] and [[experiment]]ation, and the formulation and testing of [[hypotheses]].&lt;ref&gt;
[http://www.m-w.com/dictionary/scientific%20method scientific method], ''[[Merriam-Webster|Merriam-Webster Dictionary]]''.&lt;/ref&gt;  Science, and the nature of scientific knowledge have also become the subject of [[Philosophy of science|Philosophy]].  As science itself has developed, knowledge has developed a broader usage which has been developing within biology/psychology—discussed elsewhere as [[meta-epistemology]], or [[genetic epistemology]], and to some extent related to &quot;[[theory of cognitive development]]&quot;. &amp;nbsp; &amp;nbsp; [[Image:Francis Bacon 2.jpg|thumb|150px|right|[[Sir Francis Bacon]], &quot;[[Scientia potentia est|Knowledge is Power]]&quot;]] Note that &quot;[[epistemology]]&quot; is the study of knowledge and how it is acquired. Science is &quot;the process used everyday to logically complete thoughts through inference of facts determined by calculated experiments.&quot; [[Sir Francis Bacon]] was critical in the historical development of the scientific method; his works established and popularized an inductive methodology for scientific inquiry. His famous aphorism, &quot;[[Scientia potentia est|knowledge is power]]&quot;, is found in the Meditations Sacrae (1597).&lt;ref&gt;{{cite web
| title       = Sir Francis Bacon - Quotationspage.com
| url         = http://www.quotationspage.com/quote/2060.html
| accessdate  = 2009-07-08}}&lt;/ref&gt;

Until recent times, at least in the Western tradition, it was simply taken for granted that knowledge was something possessed only by humans — and probably ''adult'' humans at that. Sometimes the notion might stretch to (ii)&amp;nbsp;''Society-as-such'', as in (e.g.) &quot;the knowledge possessed by the Coptic culture&quot; (as opposed to its individual members), but that was not assured either. Nor was it usual to consider ''unconscious'' knowledge in any systematic way until this approach was popularized by [[Sigmund Freud|Freud]].&lt;ref&gt;There is quite a good case for this exclusive specialization used by philosophers, in that it allows for in-depth study of logic-procedures and other abstractions which are not found elsewhere. However this may lead to problems whenever the topic spills over into those excluded domains—e.g. when Kant (following Newton) dismissed ''Space and Time'' as axiomatically &quot;transcendental&quot; and &quot;a priori&quot; — a claim later disproved by [[Jean Piaget|Piaget's]] clinical studies. It also seems likely that the vexed problem of &quot;''[[infinite regress]]''&quot; can be largely (but not completely) solved by proper attention to how unconscious concepts are ''actually'' developed, both during infantile learning ''and'' as inherited &quot;pseudo-transcendentals&quot; inherited from the trial-and-error of previous generations. See also &quot;[[Tacit knowledge]]&quot;.
* [[Jean Piaget|Piaget, J.]], and B.Inhelder (1927 / 1969). ''The child's conception of time''. Routledge &amp; Kegan Paul: London.
* Piaget, J., and B.Inhelder (1948 / 1956). ''The child's conception of space''. Routledge &amp; Kegan Paul: London.&lt;/ref&gt;

Other biological domains where &quot;knowledge&quot; might be said to reside, include: (iii) the ''immune system'', and (iv) in the ''DNA of the genetic code''. See the list of four &quot;epistemological domains&quot;: &amp;nbsp; [[Karl Popper|Popper]], (1975);&lt;ref&gt;[[Karl Popper|Popper, K.R.]] (1975). &quot;The rationality of scientific revolutions&quot;; in Rom Harré (ed.), ''Problems of Scientific Revolution: Scientific Progress and Obstacles to Progress in the Sciences''. Clarendon Press: Oxford.&lt;/ref&gt; and Traill (2008:&lt;ref&gt;http://www.ondwelle.com/OSM02.pdf&lt;/ref&gt;  Table&amp;nbsp;S, page&amp;nbsp;31)—also references by both to [[Niels Kaj Jerne|Niels Jerne]].

Such considerations seem to call for a separate definition of &quot;knowledge&quot; to cover the biological systems. For biologists, knowledge must be usefully ''available'' to the system, though that system need not be conscious. Thus the criteria seem to be:
* The system should apparently be dynamic and self-organizing (unlike a mere book ''on its own'').
* The knowledge must constitute some sort of representation of &quot;the outside world&quot;,&lt;ref&gt;This &quot;outside world&quot; could include other subsystems within the same organism—e.g. different &quot;mental levels&quot; corresponding to different Piagetian stages. See [[Theory of cognitive development]].&lt;/ref&gt; or ways of dealing with it (directly or indirectly).
* Some way must exist for the system to access this information quickly enough for it to be useful.

Scientific knowledge may not involve a claim to [[certainty]], maintaining [[skepticism]] means that a scientist will never be absolutely certain when they are correct and when they are not. It is thus an irony of proper [[scientific method]] that one must doubt even when correct, in the hopes that this practice will lead to greater convergence on the [[truth]] in general.&lt;ref&gt;http://philosophybites.com/2007/12/barry-stroud-on.html&lt;/ref&gt;

==Religious meaning of knowledge==
In many expressions of [[Christianity]], such as [[Catholicism]] and [[Anglicanism]], knowledge is one of the [[seven gifts of the Holy Spirit]].&lt;ref&gt;{{cite web
|url=http://www.scborromeo.org/ccc/p3s1c1a7.htm#1831
|title=Part Three, No. 1831
|work=Catechism of the Catholic Church
|accessdate=2007-04-20}}&lt;/ref&gt;

The [[Old Testament]]'s [[tree of the knowledge of good and evil]] contained the knowledge that separated Man from God: &quot;And the LORD God said, Behold, the man is become as one of us, to know good and evil…&quot; ({{bibleverse||Genesis|3:22|KJV}})

In [[Gnosticism]] divine knowledge or [[gnosis]] is hoped to be attained. In [[Thelema]] knowledge and conversation with one's Holy Guardian Angel is the purpose of life.{{citation needed|date=January 2012}}

विद्या दान (Vidya Daan) i.e. knowledge sharing is a major part of [[Dāna|Daan]], a [[Niyama|tenet]] of all [[Indian religions|Dharmic Religions]].&lt;ref&gt;[http://vhp.org/news/news-regional/delhi-seva Knowledge Donation is the primary donation]&lt;/ref&gt;
[[Hindu]] Scriptures present two kinds of knowledge, ''Paroksh Gyan'' and ''Prataksh Gyan''. ''Paroksh Gyan'' (also spelled ''Paroksha-Jnana'') is secondhand knowledge: knowledge obtained from books, hearsay, etc. ''Prataksh Gyan'' (also spelled ''Prataksha-Jnana'') is the knowledge borne of direct experience, i.e., knowledge that one discovers for oneself.&lt;ref&gt;{{cite web
|url=http://www.swami-krishnananda.org/panch/panch_07.html
|title=Chapter 7
|work=The Philosophy of the Panchadasi
|author= Swami Krishnananda
|publisher= The Divine Life Society
|accessdate=2008-07-05}}&lt;/ref&gt;  [[Jnana yoga]] (&quot;path of knowledge&quot;) is one of three main types of yoga expounded by [[Krishna]] in the [[Bhagavad Gita]].  (It is compared and contrasted with [[Bhakti#Bhakti_Yoga|Bhakti Yoga]] and [[Karma yoga]].)

In Islam, knowledge (Arabic: علم, ''ʿilm'') is given great significance. &quot;The Knowing&quot; (''al-ʿAlīm'') is one of the [[Names of God in the Qur'an|99 names]] reflecting distinct attributes of [[God in Islam|God]]. The [[Qur'an]] asserts that knowledge comes from God ({{cite quran|2|239|style=nosup|expand=no}}) and various ''[[hadith]]'' encourage the acquisition of knowledge. [[Muhammad]] is reported to have said &quot;Seek knowledge from the cradle to the grave&quot; and &quot;Verily the men of knowledge are the inheritors of the prophets&quot;. Islamic scholars, theologians and jurists are often given the title ''[[ulema|alim]]'', meaning &quot;knowledgable&quot;. {{Citation needed|date=May 2009}}

In [[Jewish]] tradition, knowledge ([[Hebrew]]: דעת ''da'ath'') is considered one of the most valuable traits a person can acquire. Observant Jews recite three times a day in the [[Amidah]] &quot;Favor us with knowledge, understanding and discretion that come from you. Exalted are you, Existent-One, the gracious giver of knowledge.&quot; The [[Tanakh]] states, &quot;A wise man gains power, and a man of knowledge maintains power&quot;, and &quot;knowledge is chosen above gold&quot;.

==See also==
{{portal|Epistemology}}
{{Wikipedia books|Epistemology}}
{{div col}}
* [[Analytic-synthetic distinction]]
* [[Wisdom]]
{{div col end}}

==References==
{{reflist|2}}

== External links  ==
{{sisterlinks|knowledge}}
*{{PhilPapers|category|knowledge}}
*{{SEP|knowledge-value|The Value of Knowledge}}
*{{InPho|taxonomy|2390}}
*{{IEP|knowledg}}

{{Philosophy topics}}
{{epistemology}}
{{Positivism}}

[[Category:Knowledge| ]]
[[Category:Concepts in epistemology]]

[[ar:معرفة]]
[[an:Conoiximiento]]
[[ast:Conocencia]]
[[zh:知识]]
"""    