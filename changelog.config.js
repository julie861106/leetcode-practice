module.exports = {
    disableEmoji: false, // 是否禁用 emoji
    format: '{emoji}{type}{scope}: {subject}', // Commit 訊息的格式
    list: ['test', 'feat', 'fix', 'chore', 'docs', 'refactor', 'style', 'ci', 'perf'], // Commit 類型的清單
    maxMessageLength: 64, // Commit 訊息的最大長度
    minMessageLength: 3, // Commit 訊息的最小長度
    questions: ['type', 'scope', 'subject', 'body', 'breaking', 'issues', 'lerna'], // 問題的清單
    scopes: [], // Commit 範圍的清單
    types: { // Commit 類型的清單
        feat: {
          description: 'A new feature',
          emoji: '✨', // Commit 類型的 emoji
          value: 'feat' // Commit 類型的值
        },
        fix: {
            description: 'A bug fix',
            emoji: '🐞',
            value: 'fix'
        },
        refactor: {
            description: 'A code change that neither fixes a bug or adds a feature',
            emoji: '🛠 ',
            value: 'refactor'
        },
        style: {
            description: 'Markup, white-space, formatting, missing semi-colons...',
            emoji: '💄',
            value: 'style'
        },
        docs: {
            description: 'Documentation only changes',
            emoji: '📚',
            value: 'docs'
        },
        ci: {
            description: 'CI related changes',
            emoji: '⏰',
            value: 'ci'
        },
        chore: {
            description: 'Build process or auxiliary tool changes', // Commit 類型的描述
            emoji: '🗯 ',
            value: 'chore'
        },
        perf: {
            description: 'A code change that improves performance',
            emoji: '⚡️',
            value: 'perf'
        },
        release: {
            description: 'Create a release commit',
            emoji: '🏹',
            value: 'release'
        },
        test: {
            description: 'Adding missing tests',
            emoji: '💍',
            value: 'test'
        },
    },
    messages: {  // Commit 的訊息描述
        type: 'Select the type of change that you\'re committing:',
        customScope: 'Select the scope this component affects:',
        subject: 'Write a short, imperative mood description of the change:\n',
        body: 'Provide a longer description of the change:\n ',
        breaking: 'List any breaking changes:\n',
        footer: 'Issues this commit closes, e.g #123:',
        confirmCommit: 'The packages that this commit has affected\n',
    },
    skipQuestions: ['breaking', 'footer']
  };
