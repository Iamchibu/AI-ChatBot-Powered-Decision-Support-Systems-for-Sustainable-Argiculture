# AGRI-BOT
# Ollama GUI: Web Interface for chatting with your local LLMs.

Ollama GUI is a web interface for [ollama.ai](https://ollama.ai/download), a tool that enables running Large
Language Models (LLMs) on your local machine.

## 🛠 Installation

### Prerequisites

1. Download and install [ollama CLI](https://ollama.ai/download).
2. Download and install [yarn](https://classic.yarnpkg.com/lang/en/docs/install/#mac-stable)
   and [node](https://nodejs.org/en/download)

```bash
ollama pull <model-name>
ollama serve
```

### Getting Started

2. Clone the repository and start the development server.

```bash
git clone https://github.com/HelgeSverre/ollama-gui.git
cd ollama-gui
yarn install
yarn dev
```

**Or use the hosted web version**, by running ollama with the following origin
command [(docs)](https://github.com/jmorganca/ollama/blob/main/docs/faq.md#how-can-i-expose-the-ollama-server)

```shell
OLLAMA_ORIGINS=https://ollama-gui.vercel.app ollama serve
```

---

## Models

For convenience and `copy-pastability`, here is a table of interesting models you might want to try out.

For a complete list of models Ollama supports, go
to [ollama.ai/library](https://ollama.ai/library 'ollama model library').

| Model                                                                                                                           | Parameters | Size  | Download                          |
|---------------------------------------------------------------------------------------------------------------------------------|------------|-------|-----------------------------------|
| Llama 2                                                                                                                         | 7B         | 3.8GB | `ollama pull llama2`              |
| Falcon                                                                                                                          | 7B         | 4.2GB | `ollama pull falcon`              |

---

- [Ollama.ai](https://ollama.ai/) - CLI tool for models.
- [LangUI](https://www.langui.dev/)
- [Python](https://www.python.org/)
- [Vue.js](https://vuejs.org/)
- [Vite](https://vitejs.dev/)
- [Tailwind CSS](https://tailwindcss.com/)
- [VueUse](https://vueuse.org/)
- [@tabler/icons-vue](https://github.com/tabler/icons-vue)

---

## 📝 License

Licensed under the MIT License. See the [LICENSE.md](LICENSE.md) file for details.
