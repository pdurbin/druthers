Druthers: crowdsourced issue ordering
=====================================

If my users had their druthers, what issues would they have me work on?

Should I ask my users to put their top few issues in order so I know what's most important to them? Yes! Druthers will help you make sense of the data, showing you either simple counts of votes or (better) weighted "points" that each issue has accumulated based on how they've ranked the issues they care about.

Run `druthers --help` for instructions.

The included input file (votes.tsv) represents 20 ordered votes on issues numbers ranging from 1 to 100.

By default, simple counting of votes is shown:

    $ ./druthers votes.tsv | head -5
    5 votes for issue 62
    4 votes for issue 55
    4 votes for issue 33
    4 votes for issue 31
    4 votes for issue 69

You can indicate that your users have put their votes in order (most important first) to get a tally of "points" for each issue:

    $ ./druthers --ordered votes.tsv | head -5 
    63 points for issue 62
    52 points for issue 20
    48 points for issue 40
    47 points for issue 84
    47 points for issue 42

If you're curious why issue 20 has so many more points than 55 you can quickly tell with `grep $ISSUE_NUMBER --color votes.tsv -C20`. The order matters! :)
