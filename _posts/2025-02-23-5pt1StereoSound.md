---
layout: post
type: snd
title: "5.1 Stereo Sound - Virtual Crossover"
image: https://i3.ytimg.com/vi/nxjFgpEjQSQ/maxresdefault.jpg
link: https://www.youtube.com/watch?v=nxjFgpEjQSQ
tags: ["audio", "stereo", "tech", "software", "virtualizing", "recommended"]
comments: true
---
It's my understanding that speaker drivers perform better when they have less sound going through them.  You may have noticed this in music when a band joins in on an instrument solo and the whole soundstage just seems to box in on itself.  So splitting audio between more drivers should improve sound quality, but making custom cross-over circuit boards is tedius and confusing for amateurs like me.

Luckily people have already been experimenting with virtual cross-overs.  I first seriously thought about this years ago when stumbling upon a plugin for [Foobar2k](https://www.foobar2000.org/) with this goal that aligns perfectly with my own: using a computers 5.1 audio to output specific frequencies to individual speakers.  I've never gotten that plugin to work as it was out of date even when I first found it, but after some digging I did find [Equalizer APO](https://equalizerapo.com/) which gives you all kind of control over your computer's audio, regardless of the media player.

So this is the setup that I'm currently enjoying.  I have a 5.1 USB DAC (it can go up to 7.1, which I'll have to take advantage of in the future) with the front channels, rear channels, and subwoofer each going into their own amplifier and connecting to different speaker boxes.  Stereo sound files natively output only to the front speakers.  So using Equalizer APO I can clone the front channels to the rear channels and mix them both to the subwoofer. Each speaker set signal can also be manipulated individually.  I have my small bookshelf speakers set with a high pass to only play frequncies above 1khz, the subwoofer to only play frequencies below 80hz, and my large speakers to play 60hz to 1400khz.

As I don't use a center channel speaker, but 5.1 audio/movie files will automatically try to output to one: I also have a second setup without any audio mods except for cloning center channel audio streams to the Left and Right channels.  Switching between the two setups is just a button press away in the task bar.

The video above doesn't make it very obvious, you can probably hear a difference in the bass, but in person the upper frequncies and vocal range are night and day different.

There is physically more space between my upper and lower frequencies, and more sound waves filling the space, so it's difficult to interpret quality, but I find it much more enjoyable to listen to for now.  I am hearing some weaknesses, but I think it's just a matter of experimenting with the cross-over frequencies because it sounds kind of like there's a hump in the audio where smooth scaling of octaves would be expected.

Regardless, I think there's a lot of potential here.  My next step would be to bypass the physical cross-overs in my speaker sets and access their drivers directly.  I'll need more amplifiers though, as without upgrading to the 7.1 output I won't be achieving my goal of having less sound across more drivers.
