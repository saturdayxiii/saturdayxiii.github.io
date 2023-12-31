---
layout: post
type: art
title: Making 7 Games as Christmas Presents (Clickbait Title)
image: https://i.postimg.cc/Fs51mKsH/tossGame.webp
link: https://i.postimg.cc/Fs51mKsH/tossGame.webp
tags:
  - christmas
  - video_game
  - design
  - programming
  - development
  - xmas
  - gdevelop
  - chat-gpt
comments: true
---
I made 7 video games as Christmas presents.  Okay, it's not actually as great as it sounds, but I will stand by that title thanks to one simple trick, and  I'm quite excited about game number 5.  I do have some personal gains to declare here, but to get the tricks out of the way: this was possible for me because of [GDevelop](https://gdevelop.io) and (surprise, surprise) Chat GPT.

I started with GDevelop, which is a game engine that specializes in web based games, with mostly codeless programming.  My first few games were graphic swaps of their car coin collecting, endless runner, and ragdoll biking templates; but I made an "original" as well.  The very first interactive tutorial on GDevelop's website was about mouse-dragging physics, so I expanded that into a scene with two characters (my nephew and his wife) with a stamina meter for each of them, and when one is full, fuel is generated for the other character which needs to be tossed across the screen while avoiding a couple of obstacles.  It's a game I swear.

Chat GPT helped me with the other games; a visual novel, a two player clicker-arm-wrestling match, and a virtual pet.  Honestly it just helped, and I learned lots.  Proof being that I had to make the games in css and html, because that's all I could ask GPT to do that I could understand.  Then it helped me learn JavaScript along the way.  By the end of each game I was working around GPTs limitations to add new features.  

I want to make specific posts for the games that took the most effort, but in any case GPT didn't have a great understanding of its own instructions.  It would often rearrange code or change it altogether and break the game.  So it really kept me focused on learning function by function.  But that didn't help when it simply didn't understand how the code was operating.

The biggest problem was trying to animate with CSS.  With CSS you can move an object from one point to another, and you can even map out more points so long as its pre-scripted.  GPT (v3.5) was convinced this could be done dynamically by just updating the destination points of the keyframes.  And maybe there really is a simple way to accomplish this, but not by any method GPT was attempting.  Once an animation runs in CSS, it's done.  Updating any destination or source coordinates just causes the object to teleport with no animation.  What I had to do was animate the object to a new spot, update the source coordinates to the new location (which requires independent maths because the source coordinates are based on the size of the parent object (for example, the size of the window) while destination coordinates are based on the height and width of the animating object), then have JavaScript delete the animation script which will load the object at its newly adjusted source location, then calculate a new destination to restart a brand new animation script.  GPT never understood this limitation and would always rewrite these extra steps out of the code.

So once I got a functioning understanding of the code, it became easiest to relegate GPT to syntax editing.  "Where's the error?", or "Is this function written correctly".  Each game code got long enough where GPT would just explain the collective features of my code rather than answer any specific question I had about it.

I never would have been able to get anywhere without Chat GPT's help, but I think I legitimately collaborated enough to have earned the credit.