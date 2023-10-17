# GitComic 💥

This script allows you to insert an icon depending on the type of updates you have made in your code.

If you want to start organizing your commits better and make them visually appealing, you're in the right place. I present you GitComic (Git Commit Icons).

## Why

After a month of trying out VSCode and getting a configuration I'm comfortable with, I've decided to go back to Nvim. 🙃

However, during my time with VSCode, I came across a specific plugin 🔌 that I loved and, after returning to the terminal, I missed it. It's a very simple plugin, but at the same time, I find it very useful, and it adds a different touch 🤩 to your Git repositories.

## Functionality

The plugin allows you to include an icon 😃 in your Git commits that visually describes the changes you've made in your repository, in addition to the comment 📝 you want to add.

For example:

Imagine you've just made changes to your .gitignore file.

``` shell
git commit -m "🙈 Added a file to ignore"
```

Or you're starting a project.

``` shell
git commit -m "🎉 Let's go for it"
```

Perhaps you've just come back from a party and feel like doing some programming.

``` shell
git commit -m "🍺 Not my best night"
```

Or, finally, you manage to pass those darn tests.

``` shell
git commit -m "✅ I'm done"
```

Those emojis aren't chosen randomly, each of them represents the essence of the changes made in that commit.

Here's a list of some more icons you can find.

🚀 Deploy stuff

🚧 Work in progress

💄 Add or update the UI and style files

🌱 Add or update seed files

🚩 Add update or remove feature flags

🥅 Catch errors

💫 Add or update animations and transitions

🔐 Add or update secrets

🔖 Release/Version tags

⬇️ Downgrade dependencies

⬆️ Upgrade dependencies

📈 Add or update analytics or track code

♻️ Refactor code

... and so on, with over 70 icons at your disposal.

## Getting started

First of all, you'll need to install the dependencies.

The script is intended to be used with <a href="https://github.com/tmux/tmux" target="_blank">tmux</a>, so if you're not familiar with it or are hesitant to use it, here's a <a href="https://www.youtube.com/watch?v=DzNmUNvnB04" target="_blank">video</a> that explains how to get started. You can also check out my own tmux configuration <a href="https://github.com/vieitesss/.mac_config/tree/main/tmux" target="_blank">here</a>.


The second and final dependency is <a href="https://github.com/junegunn/fzf" target="_blank">fzf</a>, a widely known command that allows you to select one or multiple options from various entries using advanced regular expressions.

Just follow the guides in the provided links to install both commands.

Once you have the dependencies installed, here comes the best part.

1. Clone this repository.

```shell
git clone https://github.com/vieitesss/GitComic.git
```

2. Execute the following commands.

```shell
sudo cp -r Gitcomic/gitcomic /usr/local/opt/
sudo ln -s /usr/local/opt/gitcomic/gitcomic.sh /usr/local/bin/gitcomic
```

3. Delete the repository.

```shell
rm -rf GitComic
```

4. Create a key-binding in your tmux config. You can bind any key you want.

```bash
# <prefix>g
bind-key g run-shell "gitcomic"

# C-g (without prefix)
bind-key -n C-g run-shell "gitcomic"
```

5. Start coding and bring your commits to life.

🎨 🗃️ ⚡️ 🔨 📍 💡 💸 

## Contributing

You can contact me through my social media 🕸️, sending me an email 📤, or directly make a pull request. ⁉️

If you feel that there's a missing icon for a specific description, don't hesitate to mention it. 🔫

I appreciate any kind of advice. 🙏

Press the star button if you liked it. ⭐️

