# AutoCanary

A project by Morgan Marquis-Boire & Micah Lee

(Implemented by Micah Lee)

## Overview:

A 'Warrant Canary' is a colloquial term for a regularly published statement that a service provider has not received legal process (like a national security letter) that it would be prohibited from disclosing to the public. Once a service provider does receive legal process, the speech prohibition goes into place, and the canary statement is removed.

For more information on warrant canaries see [EFF's Warrant Canary FAQ](https://www.eff.org/deeplinks/2014/04/warrant-canary-faq).

## ANATOMY OF AUTO-CANARY

(1) Warrant Canary Text
(2) Editing, Signing, and dating mechanism
(3) Scheduling of re-attesting the Warrant Canary
(4) Push mechanism for publishing the canary

At this time, parts 1 & 2 are done. We anticipate that (3) will use in built operating system scheduling mechanisms. While (4) could take the form of various CMS plugins, it is probably going to be custom for every organization and as such, currently we will offer mailing this to the webadmin or output to stdout.

AutoCanary supposes that the warrant canary will take the form of a web page. The web page will be dated and a new digitally signed copy uploaded at a regular interval. An automated scheduler runs, and at the appointed time each week, it prompts the required person (general counsel for instance) to enter in their PGP passphrase for the purposes of digitally signing the Warrant Canary. It then updates the time stamp on the document and uploads it to the webserver. The canary would stipulate that it is valid only for the interval between signing requests.

This is meant to provide attestation. The digital signing affirms that the statement is true and verifies the identity of the posting person. The frequency of signing ensures that the entity regularly attests to the truth of the canary. In the event that that a warrant is served, the person would simply stop signing given that they would no longer be able to truthfully digitally sign thecanary page.

## BACKGROUND:

The legal theory behind warrant canaries is based on the concept of compelled speech. The First Amendment protects against compelled speech in most circumstances. For example,a court held that the New Hampshire state government could not require its citizens to have "Live Free or Die" on their license plates. While the government may be able to compel silence about legal processes through a gag order, it’s much more difficult to argue that it can compel an ISP to lie by falsely stating that it has not received legal process when in fact it has.

The value of AutoCanary is that you shouldn't be forced to sign a document that you know to be untrue. Hence, if an NSL is served, the recipient would simply need to allow their canary to expire rather than sign a document that has become false.

## DISCLAIMER:

This is the big murky legal question. Frankly, nobody really knows how this would go down in court.

On one hand, some people argue that if the government imposes a non-disclosure order on you (as certain laws absolutely permit the government to do), you violate that order regardless of whether you disclose information affirmatively or by omission. And flouting a  non-disclosure order could be obstruction of justice or cause for a finding of contempt.

On the other hand, some people say they don't think the government can force you to say something -- let alone something untrue -- because the First Amendment strongly disfavors compelled speech. Plus companies aren't supposed to blatantly deceive consumers, so this would be forcing them to violate consumer protection law.

Basically, use AutoCanary at you own risk. All care and no responsibility.

<3
Morgan Marquis-Boire & Micah Lee
