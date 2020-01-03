# AutoCanary

AutoCanary is a simple, open source, desktop program for Windows, macOS, and Linux that makes the process of generating machine-readable, digitally signed warrant canary statements simpler.

A warrant canary is a published statement that a service provider has **not** received legal process that it is prohibited from disclosing to the public, such as a national security letter. Once a service provider receives a legal request that contains a gag order, the canary statement is removed. For more information, see [EFF's Warrant Canary FAQ](https://www.eff.org/deeplinks/2014/04/warrant-canary-faq).

Download Windows and macOS X binaries from the [Releases](https://github.com/firstlookmedia/autocanary/releases) page. Linux users can build from source with [these instructions](/BUILD.md).

## How it works

![AutoCanary](/screenshot.png)

Before you begin:

* Choose one person in your organization (probably your General Counsel) to be responsible for signing warrant canary statements. This person must have a PGP key.
* Choose how often you wish to issue canary statements (available options include weekly, monthly, quarterly, and semi-annually).
* Set a recurring event with a reminder in your calendar to sign your canary statement. **This is important:** failing to publish your canary statement on time could result in automated alarms ringing. If your canary stops tweeting, it may lead your users to believe you've received a gag order when you haven't.
* Create a page on your website to publish your warrant canary message, [something like this](https://help.riseup.net/en/canary).

When you run AutoCanary for the first time, first choose how frequently you'd like to publish a warrant canary message. Then choose "All good" for status" -- the other available option, "It's complicated", is there if you need it and are legally allowed to use it. If you do receive a gag order, contact a lawyer to decide how to proceed. Then write your canary statement message. You should customize it to fit your organization, and end with the name of the person who will be signing. Finally, select the PGP key that you'll be using to sign your canary statement.

If you'd like, you can include recent news headlines with each of your canary statements by checking the "Add Recent News Headlines" checkbox. This will prove that the statement was written no earlier than the date you claim it was written.

When you click `Save and Sign` all of these settings will be saved, so the next time you run AutoCanary you won't have to change anything. If you'd wish to sign a warrant canary that's different just this one time and not save your changes, you can click `One-Time Sign` instead.

After clicking a sign button, you may be prompted to enter your PGP passphrase. You'll then see your final digitally-signed warrant canary message. If it looks good to you, post it to your website.

If the person who digitally signs the canary messages knows how to update the website themselves, they can click `Copy to Clipboard`, edit the warrant canary page, and paste it. Otherwise they can click `Save to File`, and then email that file to the person in charge of updating the warrant canary page on the website. *Make sure they update it promptly to prevent the canary from expiring.*

Every time your warrant canary calendar event notifies you, open AutoCanary, generate a new canary message, and update it on your website.

# Installing

### Windows or macOS

For Windows and macOS, download the latest release from the GitHub [releases page](https://github.com/firstlookmedia/autocanary/releases).

### Debian or Ubuntu

Make sure you have `apt-transport-https` installed, and add the FLM code repository key:

```
sudo apt update
sudo apt install -y curl gnupg apt-transport-https
curl -L https://packagecloud.io/firstlookmedia/code/gpgkey | sudo apt-key add -
```

Add the repository, depending on your operating system:

- Ubuntu 18.04 (bionic)
  ```
  echo "deb https://packagecloud.io/firstlookmedia/code/ubuntu/ bionic main" | sudo tee -a /etc/apt/sources.list.d/firstlookmedia_code.list
  ```
- Ubuntu 19.04 (disco)
  ```
  echo "deb https://packagecloud.io/firstlookmedia/code/ubuntu/ disco main" | sudo tee -a /etc/apt/sources.list.d/firstlookmedia_code.list
  ```
- Ubuntu 19.10 (eoan)
  ```
  echo "deb https://packagecloud.io/firstlookmedia/code/ubuntu/ eoan main" | sudo tee -a /etc/apt/sources.list.d/firstlookmedia_code.list
  ```
- Debian 10 (buster)
  ```
  echo "deb https://packagecloud.io/firstlookmedia/code/debian/ buster main" | sudo tee -a /etc/apt/sources.list.d/firstlookmedia_code.list
  ```
- Debian 11 (bullseye)
  ```
  echo "deb https://packagecloud.io/firstlookmedia/code/debian/ bullseye main" | sudo tee -a /etc/apt/sources.list.d/firstlookmedia_code.list
  ```

Install AutoCanary:

```
sudo apt update
sudo apt install -y autocanary
```

### Fedora

We have repositories for Fedora 30 and 31. Add this repository following [these instructions](https://packagecloud.io/firstlookmedia/code/install#manual-rpm), or by running this script:

```
curl -s https://packagecloud.io/install/repositories/firstlookmedia/code/script.rpm.sh | sudo bash
```

Install AutoCanary:

```
sudo dnf install -y autocanary
```
