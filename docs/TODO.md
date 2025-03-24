# To Do

These tasks need to be completed to afford the user the full "RoboJock" experience

1. Get a server running on mini
  - "a server" means a program which is always running
2. Get that server to talk to `iTunes`
3. Add CLI app to talk to that server locally
4. Add commands to cli app which can be sent on to `iTunes':
  - play
  - pause
  - quit
  - show
  - play the playlist "Fred"
  - etc
5. Add commands to cli app which it must handle itself
  - Make a playlist of 80s dance
  - Play songs like "Go!"
6. Create a deployment pipeline
  - developer needs to be able to restart robojock on mini for
    - push code
    - merge PR
  - production machine (`mini`) when updated:
    - Get code
    - Restart robojock
  - also need a "deploy command" for
    - revert
7. Make Cover Flow the "default screen"
  - like the screen saver of that machine
  - if user does not interact (mouse/keyboard) in X minutes, then show the CoverFlow screen.
8. Show correct artist
  - iTunes CoverFlow prefers "Album Artist" for Compilations
  - Make it show "Artist" instead
9. "Double Flow"
  - Enhance (or replace) CoverFlow such that 
    8.1 Clicking on an album cover shows the back of the album
    8.2 Clicking on the back cover shows the front cover
