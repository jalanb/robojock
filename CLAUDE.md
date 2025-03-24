# robojock

This project should provide access via Python to a locally running iTunes

It should afford the same services in Python as can be used via AppleScript, and so make these available at CLI, over REST api, and via MCP server.

## The dream

We need a lot of groundwork in place before we even start thinking about these features, but the long-term vision of this project is that "Robo Jock" should mean "AI DJ".

An AI DJ should be able to
 - Play more highly rated tracks than less
 - Play an album, by choosing only some tracks from it
 - Keep new tracks in "same vibe" as recent ones
 - Take requests from users like
   - "More 80s dance"
   - "Some early punk classics please"
   - "Do you have any Daffy Duck?"
   - "CAn you make it a bit more red? A bit less blue?"

## History

The `mini` is old (OS X v10.10) because that is last verion of `iTunes` that had `CoverFlow`, which I still like best.

The music collection is older, far older.

I did actually digitise some of my first "compilation tapes" from back in the 80s, just to have the connection. But the real collection started in the 90s, and especially once I got a) headphones at work and b) widely available torrents of whatever I wanted.

The "music collection" is also more than just music - it includes thousands of small mp3 files with spoken word quotes that I pulled from movies, podcasts, youtube, ...

### Stars

Since then I have spent many decades rating songs, and now have hundreds of Gb of music, and every single track is rated, where
 - 0: not yet rated
 - 0.5: Disgusting, should be deleted!!
 - 1: Bad
 - 2: OK
 - 3: Good
 - 3.5: Good enough for the car
 - 4: Great
 - 5: All time great

Another doc will have exact definitions of these, for here it is enough to know: a 5-star scale, but it allows half-stars. And at `3.5` is the only "division": any track getting >= 3.5 gets copied on to my phone, and on to a USB stick for the car, ... 

### Colours

I have arbitrarily added "colours" to a lot of tracks in the collection.

I have used the "Genre" tag in the track's mp3 file to record my "colour" (because existing genres are arbitrary and I had not found them helpful) 

Roughly speaking the main colours are
 - Red: Rock and Classical
 - Green: Country, Irish, Acoustic
 - Blue: Dance, Pop
 - White: Spoken Word

A very imcomplete categorisation, just skimming the surface of what's possible, but enough to start with.

I noticed two tendencies when "colouring my music":
1. A _lot_ of tracks do not fit neatly into one colour, and I was soon inventing "Green/Blue" (A Country track with a lot of swing, hence "Dance") and so on.
2. Once I found an artist who was getting just a single colour for a few tracks I assigned thata colour to *all* their tracks. Should be OK for most of them (e.g. I'm fairly sure Motorhead deserves all their "red" tags) but might have been premature for some (like The Clash, who tracks will often have "Red", but not all, and certainly not exclusively)

## Environment

### Physical environment

`mini` is not really physically accessible (too much stuff to move out of the way), but it does make a mouse, a screen and a 3.5mm socket available.

That socket leads to a "3.5mm hub", whence it is connected to all the speakers/headphones in the house

The screen should be showing the CoverFlow, which allows listeners a bit more context

The mouse is behind the screen, but normally reachable, and does work

Missing: there is no keyboard attached to the machine.

### Network envirnonment

I normally use `mini` via the `Screen Sharing` app from another `mac` on the local network. This affords me "fuller" access (i.e. mouse _and_ keyboard)

I can also connect to `mini` from my iPhone, but that offers limited affordances: play/pause/search.

### machines

One machine on the network has `iTunes` running: `mini.local`

Other local machines will have a clone of the project.

Read ~/CLAUDE.md to see which machine this is

## Development

I'm a developer, working on another machine in the local network where `mini.local` is running, and providing the music we can hear over speakers, or headphones.

So, in "devspeak": this is a "dev machine" and `mini.local` is our "production machine", and we are "dogfooding", insofar as if coding errors lead to no music being played, then I get pissed off. And if "bad" music is being played then I get very pissed of.
