---
name: click-path-audit
description: >-
  Trace every button/link click call-by-call to find async races, stale closures, dead paths, and useEffect interference. Use for "clicks not working", "UI bug", or "button not responding".
---

## Step 0: Load Marketing Context
Check if `.agents/lucas-marketing-context.md` exists. Load if present — CTA analysis benefits from conversion context.

---
# Click Path Audit

Systematically trace UI interaction paths to find bugs that escape normal testing.

## The Five Bug Categories

### 1. Sequential Undo
Later step undoes earlier step's state. Find it: trace every setState in order, look for same key set twice.

### 2. Async Race
Two async operations, second completes first. Find it: any two parallel fetches triggered by same click.

### 3. Stale Closure
Handler captures old value from previous render. Find it: check all functions in click chain for closed-over variables that could have changed.

### 4. Dead Path
Code runs but has no visible effect. Find it: trace state updates through rendering conditions.

### 5. useEffect Interference
A useEffect resets state the click handler just set. Find it: all useEffects with deps touched by the click's side effects.

## Audit Process

1. **Identify Entry Point** — find the click handler, read its exact code
2. **Build the Call Tree** — trace every function call, state update, async operation
3. **Map State Changes** — list every setState/dispatch in order, flag same-key conflicts
4. **Check useEffect Interference** — for each useEffect: could the click trigger it? Does its body reset state the click sets?
5. **Report** — category, location, affected state, minimal fix

## Output Format
```
CLICK PATH AUDIT: [Component/button name]
Entry: [handler, file:line]
Call Tree: [drawn tree]
State Changes: [ordered list with conflicts flagged]
Bugs Found: [CATEGORY at location: description → fix]
Clean paths: [count]
```
