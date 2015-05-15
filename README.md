# AutoCanary

A project by Micah Lee & Morgan Marquis-Boire

## Overview

A warrant canary is a colloquial term for a published statement that a service provider has **not** received legal process that it is prohibited from disclosing to the public, such as a national security letter. Once a service provider does receive legal process that includes a non-disclosure order, the speech prohibition goes into place, and the canary statement is removed. For more information, see [EFF's Warrant Canary FAQ](https://www.eff.org/deeplinks/2014/04/warrant-canary-faq).

AutoCanary is a simple, open source, desktop program for Windows, Mac, and Linux that makes the process of generating machine-readable, digitally signed warrant canary statements simpler.

See [these instructions](/BUILD.md) to turn the source code into a binary you can run. Binaries aren't provided yet.

## How it works

![AutoCanary](/screenshot.png)

Before you begin:

* Choose one person in your organization (probably your general counsel) to be responsible for signing warrant canary statements. This person must have a PGP key.
* Choose how often you wish to issue canary statements (available options are every weekly, monthly, quarterly, and semi-annually).
* Set a recurring event with a reminder in your calendar to sign your canary statement. **This is important:** failing to publish your canary statement on time could result in automated alarms ringing. If your canary stops tweeting, it may lead your users to believe you've received a gag order when you haven't.
* Create a page on your website to publish your warrant canary message, [something like this](https://help.riseup.net/en/canary).

When you run AutoCanary, you see a window with these fields:

* Frequency: This defines the interval that the warrant canary will cover. The canary will attest to a period of time during which you have not received a gag order. This could be a specific week, month, and so on. 
* Year:  This defaults the current year. You probably won't have to change this, unless you want your warrant canary to be dated differently.
* Week / Month / Quarter / Semester: This will allow you to set the exact dates based on the 'Frequency' interval that you chose.
* Status: This should almost always be set to "All good". The other available option, "It's complicated", is there if you need it and are legally allowed to use it. If you do receive a gag order, contact a lawyer to decide how to proceed.
* Message: This starts out with a warrant canary message template. You should customize it to fit your organization, and end with the name of the person who will be signing.
* PGP Key: Select your PGP key.

When you click `Save and Sign` all of these settings will be saved, so the next time you run AutoCanary you won't have to change anything. If you'd wish to sign a warrant canary that's different just this one time and not save your changes, you can click `One-Time Sign` instead.

After clicking a sign button, you may be prompted to enter your PGP passphrase. You'll then see your final digitally-signed warrant canary message. If it looks good to you, post it to your website.

If the person who digitally signs the canary messages knows how to update the website themselves, they can click `Copy to Clipboard`, edit the warrant canary page, and paste it. Otherwise they can click `Save to File`, and then email that file to the person in charge of updating the warrant canary page on the website. *Make sure they update it promptly to prevent the canary from expiring.*

Every time your warrant canary calendar event notifies you, re-run AutoCanary, generate a new canary message, and update it on your website.

## Background

The legal theory behind warrant canaries is based on the concept of compelled speech. The First Amendment protects against this in most circumstances. For example, a court held that the New Hampshire state government could not require its citizens to have "Live Free or Die" on their license plates. While the government may be able to compel silence about legal processes through a gag order, it's much more difficult to argue that it can compel a service provider to falsely state that it has not received legal process when, in fact, it has.

The proposition behind AutoCanary is that you shouldn't be forced to sign a document that you know to be untrue. Hence, if a National Security Letter or other gag order is served, the recipient would simply allow their canary to expire rather than sign a document that has become false.

## Disclaimer

This is the big murky legal question. Frankly, nobody really knows how this would go down in court.

On one hand, some people argue that if the government imposes a non-disclosure order on you (as certain laws absolutely permit the government to do), you violate that order regardless of whether you disclose information affirmatively or by omission. Flouting a non-disclosure order could be obstruction of justice or cause for a finding of contempt.

On the other hand, some people say they don't think the government can force you to say something -- let alone something untrue -- because the First Amendment strongly disfavors compelled speech. Additionally, companies aren't supposed to blatantly deceive consumers, so anything to that effect would be forcing them to violate consumer protection law.

There is no public record of a warrant canary ever being tested in court. You should consult a lawyer to discuss the benefits and hazards before you decide whether publishing a Warrant Canary is a good course for your service. For more information about the legal issues surrounding Warrant Canaries, see: https://www.eff.org/deeplinks/2014/04/warrant-canary-faq

Basically, use AutoCanary at your own risk. All care and no responsibility.

<3

Morgan Marquis-Boire & Micah Lee
