// @ts-check
// `@type` JSDoc annotations allow editor autocompletion and type checking
// (when paired with `@ts-check`).
// See: https://docusaurus.io/docs/api/docusaurus-config

import {themes as prismThemes} from 'prism-react-renderer';

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'FLEXIcontent Documentation',
  tagline: 'The advanced CCK for Joomla!',
  favicon: 'img/favicon.ico',

  // Future flags, see https://docusaurus.io/docs/api/docusaurus-config#future
  future: {
    v4: true,
  },

  url: 'https://flexicontent.org',
  baseUrl: '/_documentation_notes/',

  organizationName: 'FLEXIcontent',
  projectName: 'flexicontent-docs',

  onBrokenLinks: 'throw',
  markdown: {
    mermaid: true,
    hooks: {
      onBrokenMarkdownLinks: 'warn',
    },
  },

  i18n: {
    defaultLocale: 'en',
    locales: ['en', 'fr'],
    localeConfigs: {
      en: {
        label: 'English',
        htmlLang: 'en',
      },
      fr: {
        label: 'Français',
        htmlLang: 'fr',
      },
    },
  },

  plugins: [
    [
      '@cmfcmf/docusaurus-search-local',
      {
        indexDocs: true,
        indexBlog: false,
        indexPages: true,
        indexDocSidebarParentCategories: 2,
        language: ['en', 'fr'],
        maxSearchResults: 10,
      },
    ],
    [
      '@docusaurus/plugin-ideal-image',
      {
        quality: 80,
        min: 640,
        max: 1280,
        steps: 3,
      },
    ],
  ],

  themes: ['@docusaurus/theme-mermaid'],

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: './sidebars.js',
          // Renseigner editUrl lorsque le dépôt Git de la documentation sera connu.
        },
        // Le blog est désactivé : la documentation ne contient qu'un menu « Ressources ».
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      }),
    ],
  ],

  themeConfig:
    /** @type {import('@docusaurus/preset-classic').ThemeConfig} */
    ({
      colorMode: {
        respectPrefersColorScheme: true,
      },
      mermaid: {
        theme: {
          light: 'neutral',
          dark: 'forest',
        },
      },
      navbar: {
        title: 'FLEXIcontent',
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'docs',
            position: 'left',
            label: 'Documentation',
          },
          {to: '/docs/ressources', label: 'Resources', position: 'left'},
          {
            href: 'https://www.flexicontent.org/',
            label: 'Official site',
            position: 'right',
          },
          {
            href: 'https://github.com/FLEXIcontent/flexicontent-cck',
            label: 'GitHub',
            position: 'right',
          },
          {
            type: 'localeDropdown',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Documentation',
            items: [
              {label: 'Introduction', to: '/docs/intro'},
              {label: 'Installation', to: '/docs/demarrage/installation'},
              {label: 'Resources', to: '/docs/ressources'},
            ],
          },
          {
            title: 'Community',
            items: [
              {label: 'Forum', href: 'https://www.flexicontent.org/forum.html'},
              {
                label: 'GitHub',
                href: 'https://github.com/FLEXIcontent/flexicontent-cck',
              },
              {
                label: 'Report an issue',
                href: 'https://github.com/FLEXIcontent/flexicontent-cck/issues',
              },
            ],
          },
          {
            title: 'Project',
            items: [
              {label: 'Official site', href: 'https://www.flexicontent.org/'},
              {
                label: 'Downloads',
                href: 'https://www.flexicontent.org/downloads/latest-version.html',
              },
              {
                label: 'Official documentation',
                href: 'https://flexicontent.org/_documentation_notes/',
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} FLEXIcontent. Built with Docusaurus.`,
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
      },
    }),
};

export default config;
