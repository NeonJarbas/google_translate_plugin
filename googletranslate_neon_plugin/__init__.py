from ovos_plugin_manager.templates.language import LanguageDetector,\
    LanguageTranslator
from google_trans_new import google_translator


class GoogleTranslator(LanguageTranslator):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.translator = google_translator()

    def translate(self, text, target=None, source=None):
        if self.boost and not source:
            source = self.default_language
        target = target or self.internal_language
        if source:
            tx = self.translator.translate(text, lang_src=source.split("-")[0],
                                           lang_tgt=target.split("-")[0])
        else:
            tx = self.translator.translate(text, lang_tgt=target.split("-")[0])
        return tx.strip()


class GoogleDetector(LanguageDetector):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.translator = google_translator()

    def detect(self, text):
        tx = self.translator.detect(text)
        return tx[0] or self.default_language

    def detect_probs(self, text):
        tx = self.translator.detect(text)
        return {"lang_code": tx[0], "lang": tx[1]}
