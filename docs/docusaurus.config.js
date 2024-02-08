// @ts-check
// `@type` JSDoc annotations allow editor autocompletion and type checking
// (when paired with `@ts-check`).
// There are various equivalent ways to declare your Docusaurus config.
// See: https://docusaurus.io/docs/api/docusaurus-config

import {themes as prismThemes} from 'prism-react-renderer';

/** @type {import('@docusaurus/types').Config} */
const config = {
  title: 'My curriculum',
  tagline: 'Atividade Ponderada Semana 01',
  favicon: 'https://rmnicola.github.io/m9-ec-encontros/icons/inteli.svg',

  // Set the production url of your site here
  url: 'https://your-docusaurus-site.example.com',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'Rizzi26', // Usually your GitHub org/user name.
  projectName: 'Atividade-Ponderada-Semana-01', // Usually your repo name.

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      /** @type {import('@docusaurus/preset-classic').Options} */
      ({
        docs: {
          sidebarPath: './sidebars.js',
          editUrl:
            'https://github.com/Rizzi26/Atividade-Ponderada-Semana-01',
            routeBasePath: '/',
        },
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
      navbar: {
        title: 'My curriculum',
        logo: {
          alt: 'Logo inteli',
          src: 'https://rmnicola.github.io/m9-ec-encontros/icons/inteli.svg',
        },
        items: [
          {
            type: 'docSidebar',
            sidebarId: 'CurriculumSidebar',
            position: 'left',
            label: 'Curriculum',
          },
          {
            href: 'https://github.com/Rizzi26/Atividade-Ponderada-Semana-01',
            label: 'GitHub',
            position: 'right',
          },
        ],
      },
      footer: {
        style: 'dark',
        links: [
          {
            title: 'Docs',
            items: [
              {
                label: 'Curriculum',
                to: '/',
              },
            ],
          },
          {
            title: 'Community',
            items: [
              {
                label: 'Instagram',
                href: 'https://www.instagram.com/rizzi_26/?next=%2F',
              },
              {
                label: 'Facebook',
                href: 'https://www.facebook.com/marcoantonio.meneguetti',
              },
              {
                label: 'linkedin',
                href: 'https://www.linkedin.com/in/marco-antonio-rizzi-620b56257/',
              },
            ],
          },
          {
            title: 'More',
            items: [
              {
                label: 'GitHub',
                href: 'https://github.com/Rizzi26',
              },
            ],
          },
        ],
        copyright: `Copyright © ${new Date().getFullYear()} My Project, Inc. Built with Docusaurus.`,
      },
      prism: {
        theme: prismThemes.github,
        darkTheme: prismThemes.dracula,
      },
    }),
};

export default config;
