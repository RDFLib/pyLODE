from dominate.tags import div, img, pre, code, p

from pylode.profiles.supermodel.model import MediaObject, ImageObject, TextObject
from pylode.profiles.supermodel.component.heading import heading
from pylode.profiles.supermodel import state


def image_component(image_object: ImageObject) -> div:
    with div() as component:
        if image_object.description:
            p(image_object.description)
        with div(_class="imageblock text-center"):
            with div(_class="content"):
                img(src=image_object.url, alt=image_object.caption)

            div(
                f"Figure {state.figure_count + 1}. {image_object.caption}",
                _class="title",
            )
            state.figure_count += 1

        return component


def text_component(text_object: TextObject) -> div:
    with div() as component:
        if text_object.description:
            p(text_object.description)
        with div(_class="listingblock"):
            with div(_class="content"):
                with pre(_class="highlight"):
                    code(text_object.text).set_attribute(
                        "data-lang", text_object.encoding_format
                    )

        return component


def example(media_object: MediaObject, heading_level: int) -> div:
    with div() as component:
        if media_object.name:
            heading(media_object.name, f"h{heading_level}", True, None)

        with div(_class=f"sect{heading_level + 1}"):
            if isinstance(media_object, ImageObject):
                image_component(media_object)
            elif isinstance(media_object, TextObject):
                text_component(media_object)

        return component
