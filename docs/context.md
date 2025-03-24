# Robojock Project Context

## Project Overview

Robojock is a project designed to interface with a locally running iTunes instance (version 10.10) on an older Mac mini. The project aims to provide remote control capabilities and eventually evolve into an "AI DJ" that can intelligently select music based on criteria like ratings, "vibe," and natural language requests.

## Session Summary

In this session, we expanded the basic iTunes interface that was initially just a skeleton with minimal functionality. We:

1. **Explored the iTunes API** through appscript to understand available capabilities
2. **Enhanced the iTunes interface** by:
   - Creating a Track class to handle track information
   - Adding methods for playback control (play, pause, next, previous)
   - Implementing playlist management
   - Adding volume control

3. **Expanded the CLI interface** to expose these new capabilities
4. **Set up a comprehensive test framework** with:
   - Proper pytest structure
   - Mock objects for appscript and iTunes
   - Unit tests for both the iTunes class and CLI commands

## Next Steps

1. **Implement Server Architecture**
   - Set up a server that runs on the mini machine
   - Create a client-server architecture to communicate with iTunes

2. **Extend iTunes Integration**
   - Add ability to search the library by attributes
   - Implement smart playlist generation based on ratings

3. **Develop "Vibe Continuity" Algorithm**
   - Create algorithms to analyze transitions between songs
   - Use color/genre tags for thematic consistency
   - Research music similarity metrics (tempo, key, structure)

4. **Natural Language Processing for Requests**
   - Implement simple pattern matching for common requests
   - Consider integration with an LLM API for more complex queries

5. **Enhanced Testing**
   - Add integration tests that run on the production machine
   - Set up CI/CD pipeline for automated testing

## Code Style and Testing Philosophy

Several key principles emerged during our discussion:

1. **Minimalism First**: Start with the minimal implementation that works, then expand.
2. **Proper Defaults**: Use `0` for integer defaults, `""` for string defaults, and reserve `None` for cases where we genuinely need a sentinel value or for mutable defaults.
3. **Clear Naming**: Use descriptive variable names (e.g., `playlist` instead of `pl`).
4. **Test Boundaries**: Don't test external libraries, just test that your code correctly interfaces with them.
5. **Test Structure**: Keep tests close to the code they test, in a `tests` directory within each package.
6. **Mock External Dependencies**: For unit tests, mock external systems (like iTunes) rather than depending on them.
7. **Different Test Levels**:
   - Unit tests: Mock dependencies
   - Integration tests: Test real components together
   - User acceptance tests: Test the entire system

## Project History

The project is built around an old Mac mini (running OS X v10.10) which is the last version of iTunes that had CoverFlow, a feature the project owner particularly likes. The music collection is extensive, with decades of carefully rated tracks:

- 0: not yet rated
- 0.5: Disgusting, should be deleted
- 1: Bad
- 2: OK
- 3: Good
- 3.5: Good enough for the car (threshold for mobile use)
- 4: Great
- 5: All time great

The owner has also developed a "color" categorization system using the Genre tag:
- Red: Rock and Classical
- Green: Country, Irish, Acoustic
- Blue: Dance, Pop
- White: Spoken Word

The physical setup involves a Mac mini that's not easily accessible but provides audio to the entire house through a 3.5mm hub. The owner normally accesses it through Screen Sharing from another Mac on the local network.

## Directory Structure

### Initial Structure
```
- /opt/clones/github/jalanb/robojock/
  - CLAUDE.md
  - LICENSE
  - README.md
  - TODO.md
  - pyproject.toml
  - robojock/
    - __init__.py
    - __main__.py
    - itunes.py
```

### Current Structure
```
- /opt/clones/github/jalanb/robojock/
  - CLAUDE.md
  - LICENSE
  - README.md
  - TODO.md
  - docs/
    - context.md
  - pyproject.toml
  - pytest.ini
  - run_tests.sh
  - robojock/
    - __init__.py
    - __main__.py
    - itunes.py
    - tests/
      - __init__.py
      - conftest.py
      - test_itunes.py
      - test_main.py
```

### Files Modified/Added

- **robojock/itunes.py**: Enhanced with a Track class and additional methods for playback control, playlist management, and volume control.
- **robojock/__main__.py**: Expanded CLI interface to expose new functionality.
- **robojock/tests/**: New directory containing test framework.
- **pytest.ini**: Configuration for pytest.
- **run_tests.sh**: Script to run tests with coverage.
- **docs/context.md**: This file, providing project context.

## Development Approach

The project follows a client-server model:
- Development happens on a "dev machine" (where this conversation occurred)
- iTunes runs on a "production machine" (mini.local)

The goal is to create a deployment pipeline that allows updates to be pushed from the dev machine to the production machine. Eventually, the system should provide a command-line interface for controlling iTunes remotely, with increasingly intelligent features like creating playlists based on mood, handling natural language requests, and maintaining "vibe continuity" between tracks.
